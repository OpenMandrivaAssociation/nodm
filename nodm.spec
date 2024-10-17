%define Werror_cflags %nil
%define debug_package %nil

Name:           nodm
Version:        0.11
Release:        2
Summary:        A display manager automatically starting an X session

Group:          Graphical desktop/Other
License:        BSD and GPLv2+
URL:            https://www.enricozini.org/sw/nodm/
Source0:        http://www.enricozini.org/sw/%{name}/%{name}_%{version}.orig.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  pam-devel
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:	pkgconfig(x11)

%description
An automatic display manager which automatically starts an X session at
system boot. It is meant for devices like smartphones, but can be used
on a regular computer as well, if the security implications are acceptable.

%prep
%setup -q

%build
%configure CFLAGS=-Wno-error
%make


%install
%makeinstall_std


%files
%doc AUTHORS COPYING README
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8.*

