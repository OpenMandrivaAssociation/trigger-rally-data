%define	oname	trigger

Summary:	Data files for the Trigger rally racing game
Name:		%{oname}-rally-data
Version:	0.6.0
Release:	%mkrel 1
Source0:	http://downloads.sourceforge.net/trigger-rally/%{oname}-rally-%{version}-data.tar.bz2
License:	GPLv2
Group:		Games/Arcade
Url:		http://sourceforge.net/projects/trigger-rally/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
Trigger is a fast-paced open source rally racing game.
This packages contains data files required by Trigger.

%prep
%setup -q -n %{oname}-rally-%{version}-data

%build

%install
%__rm -rf %{buildroot}
%__install -d %{buildroot}%{_gamesdatadir}/%{oname}
%__cp -a * %{buildroot}%{_gamesdatadir}/%{oname}
%__rm -f %{buildroot}%{_gamesdatadir}/%{oname}/*.txt
chmod 644 %{buildroot}%{_gamesdatadir}/%{oname}/trigger.config.defs

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt README-stereo.txt
%{_gamesdatadir}/%{oname}


