# Network Device Configuration Backup with
This repository houses Python scripts for automating the backup process of configurations for Cisco, Palo Alto, Juniper, F5, and Fortinet devices. The scripts are designed to execute daily using GitHub Actions and save backups with redundancy in virtual machines (VMs) located across different data centers. Additionally, access credentials for both network devices and VMs are securely stored in GitHub Secrets, ensuring a streamlined and secure backup strategy.

# Features
Daily Automated Backups: Utilize GitHub Actions to schedule daily backups without manual intervention.
Support for Various Network Devices: Backup configurations for Cisco, Palo Alto, Juniper, F5, and Fortinet devices.
Redundant Storage in VMs: Store backups redundantly in VMs on QTS ATL and QTS CHI for increased reliability.
Secure Credential Management: Access credentials for network devices and VMs are securely stored using GitHub Secrets.
Easily Configurable: Customize backup settings and schedule according to specific requirements.
# Usage
Fork or clone this repository to your GitHub account or local machine.

git clone https://github.com/stone-payments/network-core-backup

Configure access credentials for network devices and VMs in the GitHub Secrets settings of your repository. Required secrets include:

DEVICE_USERNAME: Username for accessing network devices.  
DEVICE_PASSWORD: Password for accessing network devices.  
VM_USERNAME: Username for logging into VMs.  
VM_PASSWORD: Password for logging into VMs.  

Customize backup settings in the backup.py script if necessary. You may adjust backup schedules, storage locations, or any other parameters based on your requirements.

Ensure that Python scripts (cisco.py or any oder vendor.py any supporting scripts) are correctly configured and functional.

Commit and push any changes to your repository to trigger the GitHub Actions workflow.

Monitor the execution of the backup process through GitHub Actions logs.

# GitHub Actions Workflow
The repository comes pre-configured with a GitHub Actions workflow (/.github/workflows/backup.yml) responsible for executing the backup process daily. The workflow includes steps to:

Checkout the repository.
Install dependencies.
Execute the backup script ("backup.py").
Handle any errors and provide appropriate notifications.
You can customize the workflow to fit your specific needs by modifying the workflow file.

# Contributing
Contributions to this project are welcome. If you encounter any issues, have suggestions for improvements, or wish to add support for additional devices, feel free to open an issue or submit a pull request.



Note: Always ensure that you have proper authorization and permissions before attempting to access and backup network device configurations. Additionally, handle access credentials securely and avoid exposing sensitive information. 