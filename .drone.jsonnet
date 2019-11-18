local PipelineLinting = {
    kind: "pipeline",
    name: "linting",
    platform: {
        os: "linux",
        arch: "amd64",
    },
    steps: [
        {
            name: "later",
            image: "xoxys/ansible-later:latest",
            commands: [
                "ansible-later",
            ],
        },
    ],
    trigger: {
        ref: ["refs/heads/master", "refs/tags/**", "refs/pull/**"],
    },
};

local PipelineTesting(scenario="ubuntu1804") = {
    kind: "pipeline",
    name: "testing-" + scenario,
    platform: {
        os: "linux",
        arch: "amd64",
    },
    concurrency: {
        limit: 1,
    },
    workspace: {
        base: "/drone/src",
        path: "owncloud",
    },
    steps: [
        {
            name: "molecule",
            image: "xoxys/molecule:hcloud-linux-amd64",
            environment: {
                HCLOUD_TOKEN: { from_secret: "hcloud_token" },
                USER: "root",
                PY_COLORS: 1,
            },
            commands: [
                "/bin/bash /docker-entrypoint.sh",
                "molecule test -s " + scenario,
            ],
        },
    ],
    trigger: {
        ref: ["refs/heads/master", "refs/tags/**"],
    },
    depends_on: [
        "linting",
    ],
};

local PipelineDocumentation = {
    kind: "pipeline",
    name: "documentation",
    platform: {
        os: "linux",
        arch: "amd64",
    },
    steps: [
        {
            name: "generate",
            image: "xoxys/ansible-doctor:latest",
            environment: {
                ANSIBLE_DOCTOR_LOG_LEVEL: "INFO",
                ANSIBLE_DOCTOR_FORCE_OVERWRITE: true,
                ANSIBLE_DOCTOR_EXCLUDE_FILES: "molecule/",
                ANSIBLE_DOCTOR_CUSTOM_HEADER: "HEADER.md",
            },
        },
        {
            name: "commit",
            image: "plugins/git-action:latest",
            settings: {
                actions: [
                    "commit",
                    "push"
                ],
                author_email: { from_secret: "github_author_email" },
                author_name: "ownClouders",
                branch: "master",
                message: "[SKIP CI] update readme",
                remote: "https://github.com/owncloud-ansible/owncloud",
                netrc_machine:" github.com",
                netrc_username: { from_secret: "github_username" },
                netrc_password: { from_secret: "github_token" },
            },
            when: {
                ref: ["refs/heads/master"],
            },
        },
    ],
    trigger: {
        ref: ["refs/heads/master", "refs/tags/**", "refs/pull/**"],
    },
    depends_on: [
        "testing-ubuntu1804",
        "testing-centos7"
    ],
};

local PipelineNotification = {
    kind: "pipeline",
    name: "notification",
    platform: {
        os: "linux",
        arch: "amd64",
    },
    steps: [
        {
            name: "notify",
            image: "plugins/slack:1",
            settings: {
                webhook: { from_secret: "slack_webhook_private" },
                channel: { from_secret: "slack_channel" },
            },
        },
    ],
    trigger: {
        ref: ["refs/heads/master", "refs/tags/**"],
        status: ["success", "failure"],
    },
    depends_on: [
        "linting",
        "testing-ubuntu1804",
        "testing-centos7",
        "documentation",
    ],
};


[
    PipelineLinting,
    PipelineTesting(scenario="ubuntu1804"),
    PipelineTesting(scenario="centos7"),
    PipelineDocumentation,
    PipelineNotification,
]
