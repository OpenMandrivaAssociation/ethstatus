Name:           ethstatus
Version:        0.4.3
Release:        1
Summary:        Console-based ethernet statistics monitor
Group:          Monitoring
License:        GPLv2+
URL:            http://packages.debian.org/stable/net/ethstatus
Source0:        http://ftp.de.debian.org/debian/pool/main/e/%{name}/%{name}_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ncurses-devel

%description
EthStatus is a simple, easy to use program for displaying commonly 
needed / wanted statistics in real time about ingoing and outgoing
traffic that is usually hard to find, with a simple, efficient
interface.  


%prep
%setup -q


%build
%make

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc CHANGELOG COPYRIGHT README THANKS
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}


%changelog
* Thu Feb 09 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.3-1
+ Revision: 772244
- imported package ethstatus

