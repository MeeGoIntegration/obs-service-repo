Name:       obs-service-repo

Summary:    Repo service designed for droid-hal-device builds
Version:    0.9
Release:    1
Group:      Development/Tools
BuildArch:  noarch
License:    GPLv2
URL:        https://git.merproject.org/mer-obs/obs-repo-service
Source0:    %{name}-%{version}.tar.xz
Requires:   obs-source_service
Requires:   git-core
Requires:   python

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/obs/service/
mkdir -p %{buildroot}/etc/cron.d/
cp repo %{buildroot}/usr/lib/obs/service/
cp repo.service %{buildroot}/usr/lib/obs/service/
cp repo-service-cronjob %{buildroot}/usr/lib/obs/service/
cp repo.crontab %{buildroot}/etc/cron.d/

mkdir -p %{buildroot}/%{_bindir}
cp repo.py %{buildroot}/%{_bindir}/repo


%files
%defattr(-,root,root,-)
/usr/lib/obs/
/etc/cron.d/
%defattr(755,root,root,-)
/usr/lib/obs/service/repo
/usr/lib/obs/service/repo-service-cronjob
%{_bindir}/repo
