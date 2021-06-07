local PipelineLinting = {
  kind: 'pipeline',
  name: 'linting',
  platform: {
    os: 'linux',
    arch: 'amd64',
  },
  steps: [
    {
      name: 'later',
      image: 'thegeeklab/ansible-later',
      commands: [
        'ansible-later',
      ],
    },
    {
      name: 'python-format',
      image: 'python:3.9',
      environment: {
        PY_COLORS: 1,
      },
      commands: [
        'pip install -qq yapf',
        'yapf -dr ./',
      ],
    },
    {
      name: 'python-flake8',
      image: 'python:3.9',
      environment: {
        PY_COLORS: 1,
      },
      commands: [
        'pip install -qq flake8',
        'flake8',
      ],
    },
  ],
  trigger: {
    ref: ['refs/heads/master', 'refs/tags/**', 'refs/pull/**'],
  },
};

local PipelineTesting(scenario='ubuntu1804') = {
  kind: 'pipeline',
  name: 'testing-' + scenario,
  platform: {
    os: 'linux',
    arch: 'amd64',
  },
  concurrency: {
    limit: 1,
  },
  workspace: {
    base: '/drone/src',
    path: 'owncloud',
  },
  steps: [
    {
      name: 'molecule',
      image: 'thegeeklab/molecule:3',
      environment: {
        HCLOUD_TOKEN: { from_secret: 'hcloud_token' },
        USER: 'root',
        PY_COLORS: 1,
      },
      commands: [
        'molecule test -s ' + scenario,
      ],
    },
  ],
  trigger: {
    ref: ['refs/heads/master', 'refs/tags/**', 'refs/pull/**'],
  },
  depends_on: [
    'linting',
  ],
};

local PipelineDocumentation = {
  kind: 'pipeline',
  name: 'documentation',
  platform: {
    os: 'linux',
    arch: 'amd64',
  },
  steps: [
    {
      name: 'generate',
      image: 'thegeeklab/ansible-doctor',
      environment: {
        ANSIBLE_DOCTOR_LOG_LEVEL: 'INFO',
        ANSIBLE_DOCTOR_FORCE_OVERWRITE: true,
        ANSIBLE_DOCTOR_EXCLUDE_FILES: 'molecule/',
        ANSIBLE_DOCTOR_TEMPLATE: 'hugo-book',
        ANSIBLE_DOCTOR_OUTPUT_DIR: '_docs/',
      },
    },
    {
      name: 'publish',
      image: 'plugins/gh-pages',
      settings: {
        username: { from_secret: 'github_username' },
        password: { from_secret: 'github_token' },
        pages_directory: '_docs/',
        target_branch: 'docs',
      },
      when: {
        ref: ['refs/heads/master'],
      },
    },
    {
      name: 'trigger',
      image: 'plugins/downstream',
      settings: {
        server: 'https://drone.owncloud.com',
        token: { from_secret: 'drone_token' },
        fork: true,
        repositories: [
          'owncloud-ansible/owncloud-ansible.github.io@source',
        ],
      },
      when: {
        ref: ['refs/heads/master'],
      },
    },
  ],
  trigger: {
    ref: ['refs/heads/master', 'refs/tags/**', 'refs/pull/**'],
  },
  depends_on: [
    'testing-ubuntu1804',
    'testing-centos7',
    'testing-centos8',
    'testing-opensuse15',
  ],
};

local PipelineNotification = {
  kind: 'pipeline',
  name: 'notification',
  platform: {
    os: 'linux',
    arch: 'amd64',
  },
  steps: [
    {
      name: 'notify',
      image: 'plugins/slack:1',
      settings: {
        webhook: { from_secret: 'slack_webhook_private' },
        channel: { from_secret: 'slack_channel' },
      },
    },
  ],
  trigger: {
    ref: ['refs/heads/master', 'refs/tags/**'],
    status: ['success', 'failure'],
  },
  depends_on: [
    'linting',
    'testing-ubuntu1804',
    'testing-centos7',
    'testing-centos8',
    'testing-opensuse15',
    'documentation',
  ],
};


[
  PipelineLinting,
  PipelineTesting(scenario='ubuntu1804'),
  PipelineTesting(scenario='ubuntu2004'),
  PipelineTesting(scenario='centos7'),
  PipelineTesting(scenario='centos8'),
  PipelineTesting(scenario='opensuse15'),
  PipelineDocumentation,
  PipelineNotification,
]
