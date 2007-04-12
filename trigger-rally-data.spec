%define oname trigger
%define name %{oname}-rally-data
%define version 0.5.2
%define release %mkrel 1

%define distname %{oname}-%{version}-data

Summary: Data files for the Trigger rally racing game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/trigger-rally/%{distname}.tar.bz2
License: GPL
Group: Games/Arcade
Url: http://sourceforge.net/projects/trigger-rally/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
Trigger is a fast-paced open source rally racing game.
This packages contains data files required by Trigger.

%prep
%setup -q -n %{distname}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_gamesdatadir}/%{oname}
cp -a * %{buildroot}%{_gamesdatadir}/%{oname}
rm -f %{buildroot}%{_gamesdatadir}/%{oname}/*.txt
chmod 644 %{buildroot}%{_gamesdatadir}/%{oname}/trigger.config.defs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt README-stereo.txt
%{_gamesdatadir}/%{oname}


