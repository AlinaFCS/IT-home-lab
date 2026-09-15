Import-Module ActiveDirectory;
$users = Import-Csv -Path "C:\Users\Administrator\Desktop\new_employees.csv";
foreach ($user in $users) {
$securePassword = ConvertTo-SecureString $user.Password -AsPlainText -Force;
$upn = "$($user.Username)@lab.local";
$ouPath = "OU=$($user.OU),DC=lab,DC=local";
$params = @{ Name = "$($user.FirstName) $($user.LastName)"; GivenName = $user.FirstName; Surname = $user.LastName; SamAccountName = $user.Username; UserPrincipalName = $upn; Path = $ouPath; AccountPassword = $securePassword; Enabled = $true; ChangePasswordAtLogon = $true };
New-ADUser @params;
Write-Host "Created user: $($user.FirstName) $($user.LastName)";
}
