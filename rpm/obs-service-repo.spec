Name:       obs-service-repo

Summary:    Repo service designed for droid-hal-device builds
Version:    0.4
Release:    1
Group:      Development/Tools
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
cp repo %{buildroot}/usr/lib/obs/service/
cp repo.service %{buildroot}/usr/lib/obs/service/

mkdir -p %{buildroot}/%{_bindir}
cp repo.py %{buildroot}/%{_bindir}/repo


%files
%defattr(-,root,root,-)
/usr/lib/obs/
%defattr(755,root,root,-)
/usr/lib/obs/service/repo
%{_bindir}/repo
