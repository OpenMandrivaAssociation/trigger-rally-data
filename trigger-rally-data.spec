%define	oname	trigger

Summary:	Data files for the Trigger rally racing game
Name:		%{oname}-rally-data
Version:	0.6.0
Release:	2
Source0:	http://downloads.sourceforge.net/trigger-rally/%{oname}-rally-%{version}-data.tar.bz2
License:	GPLv2
Group:		Games/Arcade
Url:		http://sourceforge.net/projects/trigger-rally/
BuildArch:	noarch

%description
Trigger is a fast-paced open source rally racing game.
This packages contains data files required by Trigger.

%prep
%setup -q -n %{oname}-rally-%{version}-data

%build

%install
install -d %{buildroot}%{_gamesdatadir}/%{oname}
cp -ra * %{buildroot}%{_gamesdatadir}/%{oname}
rm -f %{buildroot}%{_gamesdatadir}/%{oname}/*.txt
chmod 644 %{buildroot}%{_gamesdatadir}/%{oname}/trigger.config.defs

%files
%doc README.txt README-stereo.txt
%{_gamesdatadir}/%{oname}
