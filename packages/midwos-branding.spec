
Name:           midwos-branding
Version:        1.0.0
Release:        1%{?dist}
Summary:        Official desktop wallpapers for MidwOS Horizon 1.0

License:        LicenseRef-Proprietary
URL:            https://restudiosoftwarelaboratories.github.io/Restudio-OSes-Docs/

BuildArch:      noarch

Source0:        lightscape-unsplash.jpg
Source1:        royce-fonseca-unsplash.jpg
Source2:        sebastian-unrau-unsplash.jpg

%description
Official desktop wallpapers for MidwOS Horizon 1.0,
maintained by Restudio Software Laboratories.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/backgrounds/midwos

install -m 0644 %{SOURCE0} \
    %{buildroot}%{_datadir}/backgrounds/midwos/lightscape-unsplash.jpg

install -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/backgrounds/midwos/royce-fonseca-unsplash.jpg

install -m 0644 %{SOURCE2} \
    %{buildroot}%{_datadir}/backgrounds/midwos/sebastian-unrau-unsplash.jpg

%files
%dir %{_datadir}/backgrounds/midwos
%{_datadir}/backgrounds/midwos/lightscape-unsplash.jpg
%{_datadir}/backgrounds/midwos/royce-fonseca-unsplash.jpg
%{_datadir}/backgrounds/midwos/sebastian-unrau-unsplash.jpg

%changelog
* Sat Oct 31 2026 Restudio Software Laboratories
- Initial release of MidwOS branding package.
