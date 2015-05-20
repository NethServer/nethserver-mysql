Summary: NethServer MySQL configuration and templates.
Name: nethserver-mysql
Version: 1.0.7
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: mariadb-server, perl-Expect
Requires: nethserver-base
BuildRequires: nethserver-devtools

%description
This package adds necessary startup and configuration items for
mysql.

%prep
%setup

%build
mkdir -p root/etc/e-smith/sql/init
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Wed Oct 22 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.7-1.ns6
- MySQL backup doesn't fail if root password is not set - Bug #2906 [NethServer]

* Wed Aug 20 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.6-1.ns6
- Backup: pre-backup-data event fails if mysqldump can't acquire lock - Bug #2791 [NethServer]

* Wed Dec 18 2013 Davide Principi <davide.principi@nethesis.it> - 1.0.5-1.ns6
- Service mysql.init does not support chkconfig - Bug #2350 [NethServer]

* Mon Jul 29 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.4-1.ns6
- Remove unused Runlevels prop  #2067
- Correctly start mysqld on first install  #2043

* Fri Jul 12 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.3-1.ns6
- Backup: implement and document full restore #2043

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
• Rebuild for automatic package handling. #1870

* Tue Mar 19 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Add backup configuration
- Add migration code

* Fri Jan 18 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- First release

