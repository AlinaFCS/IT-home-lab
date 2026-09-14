# Active Directory Lab: Domain Controller, Client Join & Group Policy

A hands-on home lab built in VirtualBox to practice core Windows Server / Active
Directory administration tasks: standing up a domain controller, organizing users
into OUs and security groups, joining a Windows 11 client to the domain, and
enforcing a Group Policy restriction end-to-end.

## Environment

| Component | Details |
|---|---|
| Hypervisor | Oracle VirtualBox 7.2.6 |
| Domain Controller | Windows Server 2022 Standard (Evaluation) — hostname `DC01` |
| Client | Windows 11 Pro — hostname `Client01` |
| Domain | `lab.local` |
| Network | VirtualBox Internal Network (`intnet`), static IPs on `192.168.10.0/24` |
| DC IP / DNS | `192.168.10.1` |
| Client IP | `192.168.10.2` |

## Objective

This lab was built to practice the kind of day-to-day tasks an entry-level IT
support role involves: setting up devices, troubleshooting hardware/software
issues, managing a small network, and applying security policies — using a
real (if small-scale) Active Directory environment rather than just reading
about one.

## What Was Built

1. **Domain Controller setup** — Installed Windows Server 2022, configured a
   static IP, and promoted the server to a new Active Directory forest
   (`lab.local`) using the Active Directory Domain Services role.
2. **Organizational structure** — Created OUs (`Employees`, `Managers`, `IT`)
   and populated them with test user accounts.
3. **Security groups** — Created `G_employees`, `G_Managers`, and `IT`
   security groups and assigned users to them, mirroring how access would be
   managed in a real organization.
4. **Client domain join** — Installed Windows 11 Pro on a second VM,
   configured networking, and joined it to the `lab.local` domain.
5. **Group Policy** — Created a GPO linked to the `Employees` OU that blocks
   access to Control Panel / PC Settings, and verified it took effect on the
   client.

## Walkthrough

### 1. Promoting the Server to a Domain Controller

Used the Active Directory Domain Services Configuration Wizard to create a
new forest and root domain (`lab.local`).

![AD DS Configuration Wizard](screenshots/01-dcpromo-wizard.png)

### 2. Verifying Network & DNS Configuration

Confirmed the server had a static IP and was acting as its own DNS server —
a requirement for AD DS.

![DNS/network config on DC01](screenshots/02-dns-network-config.png)

### 3. Confirming the Domain Controller Registered Correctly

Checked **Active Directory Users and Computers** to confirm `DC01` appears
under the `Domain Controllers` container.

![Domain controller verification](screenshots/03-domain-controller-verification.png)

### 4. Building the OU Structure

Created `Employees` and `Managers` OUs under `lab.local` to organize
accounts by role.

![Initial OU structure](screenshots/04-ou-structure-initial.png)

### 5. Creating User Accounts

Created the first domain user account (`Ivan Hola`) inside the `Employees` OU.

![First user created](screenshots/05-first-user-created.png)

Added two more employee accounts (`Linda Rich`, `Nata Lu`) to round out the
`Employees` OU.

![Employees OU with multiple users](screenshots/06-employees-users.png)

### 6. Creating Security Groups

Created `G_employees` and assigned the employee accounts as members.

![Employees security group](screenshots/07-employees-security-group.png)

Created `G_Managers` for the management-level accounts.

![Managers security group](screenshots/08-managers-security-group.png)

Added an `IT` OU to the structure, separating IT staff from general staff.

![OU structure with IT added](screenshots/09-ou-structure-with-it.png)

Created the `IT` security group with a dedicated IT account (`Ron Delon`).

![IT security group](screenshots/10-it-security-group.png)

### 7. Joining the Windows 11 Client to the Domain

From the client, changed domain membership from `WORKGROUP` to `lab.local`,
authenticating with domain admin credentials.

![Joining Client01 to the domain](screenshots/11-domain-join-credentials.png)

Confirmation that the join succeeded.

![Domain join success](screenshots/12-domain-join-success.png)

### 8. Verifying Network Connectivity

Pinged the domain controller from the client to confirm the two VMs could
reach each other over the internal network.

![Ping test from client to DC](screenshots/13-client-server-ping-test.png)

### 9. Enforcing a Group Policy

Created a new GPO, **"Block Control Panel - Employees"**, linked to the
`Employees` OU.

![GPO creation](screenshots/14-gpo-creation.png)

On the client, forced an immediate policy refresh instead of waiting for the
default refresh interval.

![gpupdate /force](screenshots/15-gpupdate-force.png)

Confirmed the restriction took effect — Control Panel access is blocked for
users in the `Employees` OU.

![GPO verified — Control Panel blocked](screenshots/16-gpo-verification-blocked.png)

## Skills Demonstrated

- Installing and configuring Windows Server 2022
- Promoting a server to a Domain Controller (AD DS, DNS)
- Static IP configuration and basic network troubleshooting
- Organizational Unit (OU) design
- Creating and managing users and security groups
- Joining a Windows client to a domain
- Creating and applying Group Policy Objects (GPOs)
- Verifying policy application with `gpupdate /force`
- General VM/hypervisor troubleshooting (see below)

## Troubleshooting Notes

A few real issues came up during the build — documenting them here since
diagnosing this kind of thing is a core IT support skill:

- **Black screen on Windows 11 VM boot (VirtualBox 7.2.x):** A known bug
  where Windows 11 guests hang on a black screen with 2 vCPUs assigned.
  Fixed by increasing the VM to 3–4 virtual CPUs.
- **Windows 11 setup requiring a Microsoft account:** Newer builds hide the
  offline-account option. Bypassed via `Shift+F10` during OOBE and running
  `start ms-cxh:localonly` to force a local account setup screen.
- **Insufficient RAM for simultaneous VMs:** Running both VMs with 4 GB RAM
  each exceeded the host's 8 GB. Reduced DC RAM to 2 GB (sufficient for a
  small lab) while keeping the client at 4 GB (Windows 11's minimum
  requirement).

## Next Steps

Planned follow-up labs (kept separate from this one to stay focused):

- Shared folder with NTFS permissions managed through security groups
- Domain-wide password policy configuration
- Remote Desktop access between DC and client
- Scenario-based troubleshooting labs (broken GPO, failed domain login, etc.)
