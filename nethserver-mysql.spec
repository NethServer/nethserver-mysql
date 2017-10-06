Summary: NethServer MySQL configuration and templates.
Name: nethserver-mysql
Version: 1.1.3
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: mariadb-server, perl-Expect
Requires: nethserver-base

BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

BuildRequires: nethserver-devtools

URL: %{url_prefix}/%{name}

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
%attr(0644,root,root) %ghost %{_sysconfdir}/my.cnf.d/nethserver.cnf

%post
%systemd_post mysqld.service

%preun
%systemd_preun mysqld.service

%postun
%systemd_postun

%changelog
* Fri Oct 06 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.3-1
- Use mysqld_safe for stopping mariadb instances

* Wed Sep 13 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1
- MariaDB (MySQL): do not restore root password within configuration backup - Bug NethServer/dev#5339

* Fri Jan 20 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1
- restore-data: mysql - Can't change root password - Bug NethServer/dev#5197

* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.1.0-1
- First NS7 release

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

