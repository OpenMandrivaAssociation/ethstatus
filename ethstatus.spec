Summary:	Console-based ethernet statistics monitor
Name:		ethstatus
Version:	0.4.3
Release:	1
Group:		Monitoring
License:	GPLv2+
Url:		http://packages.debian.org/stable/net/ethstatus
Source0:	http://ftp.de.debian.org/debian/pool/main/e/%{name}/%{name}_%{version}.tar.gz
Patch0:		ethstatus-0.4.3-flags.patch
BuildRequires:	pkgconfig(ncurses)

%description
EthStatus is a simple, easy to use program for displaying commonly 
needed / wanted statistics in real time about ingoing and outgoing
traffic that is usually hard to find, with a simple, efficient
interface.

%prep
%setup -q
%apply_patches

%build
%setup_compile_flags
%make

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc CHANGELOG COPYRIGHT README THANKS
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}

