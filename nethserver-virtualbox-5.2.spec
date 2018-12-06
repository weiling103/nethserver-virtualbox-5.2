%define name nethserver-virtualbox-5.2
%define version 5.2.0
%define release 1
%define rpmver   5.2.0
Summary: nethserver rpm to install virtualbox
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source: %{name}-%{version}.tar.gz
License: GNU GPL version 3
URL: http://mirror.de-labrusse.fr
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildArchitectures: noarch
BuildRequires: nethserver-devtools
Requires: VirtualBox-5.2
Requires: gcc 
Requires: make
Requires: kernel-devel
Requires: kernel-headers
Requires: dkms
AutoReqProv: no

%description
nethserver rpm to install virtualbox

%changelog
* Thu Dec 06 2018 stephane de Labrusse <stephdl@de-labrusse.fr> 5.2.0-1
- Initial commit to nethserver

* Wed Aug 07 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 5.0.0-3
- vboxweb-service start now at S99

* Thu Aug 06 2015 stephane de labrusse <stephdl@de-labrusse.fr> 5.0.0-2
- require virtualbox-5.0

* Wed Mar 19 2014 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.1-1
- added a script to verify if the vboxdrv module is compiled for the kernel used by the system

* Mon Dec 30 2013 JP Pialasse <tests@pialasse.com> 4.3.0-5
- changing naming of contrib for import into buildsys

* Tue Nov 05 2013 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.0-4
- change name to match the virtualbox version

* Sat Oct 19 2013 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.0-3
- Initial release

%prep
%setup
%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
  --file /usr/libexec/nethserver/vboxdrv-CompileModule 'attr(0750,root,root)' \
> %{name}-%{version}-filelist
echo "%doc COPYING"  >> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%pre

%preun

%post

%postun
%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
