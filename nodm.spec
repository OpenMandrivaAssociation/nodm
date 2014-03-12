Name:           nodm
Version:        0.11
Release:        1%{?dist}
Summary:        A display manager automatically starting an X session

Group:          Graphical desktop/Other
License:        BSD and GPLv2+
URL:            http://www.enricozini.org/sw/nodm/
Source0:        http://www.enricozini.org/sw/%{name}/%{name}_%{version}.orig.tar.gz
Source1:	nodm.pamd
Patch0:		Makefile.am.diff
Patch1:		Makefile.in.diff
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
%patch0 -p1
%patch1 -p1

# run autogen.sh since we patch configure.ac
# but don't run configure twice
NOCONFIGURE=true ./autogen.sh


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%{_mandir}/man8/%{name}.8.xz


%changelog
