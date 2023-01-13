# Descisions Log

## Requirements

* Alle VM disks moeten encrypted zijn.
De webserver moet dagelijks gebackupt worden. De backups moeten 7 dagen behouden worden.

Use EBS volumes and encrypt them using data keys generated by AWS KMS. Then use AWS Backup to manage the backups.

* De webserver moet op een geautomatiseerde manier geïnstalleerd worden.

With CDK, launch the webserver using snapshots or launch EC2 instances with user data.

* De admin/management server moet bereikbaar zijn met een publiek IP.

Option 1: Launch the admin server in a private subnet and then connect it to a public subnet with a NAT gateway. 

Option 2: Launch the admin server in a public subnet.

* De admin/management server moet alleen bereikbaar zijn van vertrouwde locaties (office/admin’s thuis)

Use network ACLs to specify and allow the IP addresses of the office and admin's home network. Block all other IP addresses.

* De volgende IP ranges worden gebruikt: 10.10.10.0/24 & 10.20.20.0/24

Use these IP ranges.

* Alle subnets moeten beschermd worden door een firewall op subnet niveau.

Use network ACLs.

* SSH of RDP verbindingen met de webserver mogen alleen tot stand komen vanuit de admin server.

Only allow incoming SSH/RDP connections from the admin VPC connection.

* Wees niet bang om verbeteringen in de architectuur voor te stellen of te implementeren, maar maak wel harde keuzes, zodat je de deadline kan halen.


![screenshot](/00_includes/Project/techgrounds-schematic.PNG)  