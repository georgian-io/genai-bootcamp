# GCP Specific resources
---
# Links
- [Georgian instructions for creating a hackathon GCP project.](https://app.clickup.com/1236149/v/dc/15q5n-49707/15q5n-78385)
- [How to share Disk across instances (max 2)](https://cloud.google.com/compute/docs/disks/sharing-disks-between-vms#gcloud)

# Connecting to instances
To access VMs install [gcloud cli](https://cloud.google.com/sdk/docs/install). After init on your machine.

```
gcloud init
```

After authorization is complete you can ssh into VM, to test this run:
```
gcloud compute ssh --zone "<region>" "<instance-name>"  --project "<project-name>"
```
To use ssh, rsync, and visual studio code remote ssh configure ssh:
```
gcloud compute config-ssh --project "<project-name>"
```
Check correctness:
```
ssh <instance-name>.<region>.<project-name>
```

# Using with VS Code
```
gcloud compute config-ssh --project "<project-name>"
```

```
ssh <instance-name>.<region>.<project-name> -A
```
Check out your ssh config
```
code ~/.ssh/config
```
Towards the bottom, it should now contain a host config similar to this:
```
Host <instance-name>.<region>.<project-name>
    HostName xx.xx.xx.xxx
    IdentityFile /Users/<your-user>/.ssh/google_compute_engine
    UserKnownHostsFile=/Users/<your-user>/.ssh/google_compute_known_hosts
    HostKeyAlias=compute.1234567890123456789
    IdentitiesOnly=yes
    CheckHostIP=no
```
If it's missing fields, add them from the info in the GCP console.

After this, go to VS Code, install the [Remote SSH App](https://code.visualstudio.com/docs/remote/ssh-tutorial).

Now, when you open the app side display (left side, selected Remote from top dropdown) you should see `<instance-name>` as one of the options and should be able to connect to it.

*Optionally*, you can also install the [Google Cloud VScode App](https://marketplace.visualstudio.com/items?itemName=GoogleCloudTools.cloudcode&ssr=false#overview). This gives you lots of controls and google cloud functions directly from VS Code. It is recommended you install this on you **local** VS code version, not the remote instance.