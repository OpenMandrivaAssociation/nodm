Name:           nodm
Version:        0.11
Release:        1%{?dist}
Summary:        A display manager automatically starting an X session

Group:          User Interface/X
License:        BSD and GPLv2+
URL:            http://www.enricozini.org/sw/nodm/
Source0:        http://www.enricozini.org/sw/%{name}/%{name}_%{version}.orig.tar.gz
Source1:        nodm.pamd
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  pam-devel
BuildRequires:  libX11-devel
BuildRequires:  help2man
BuildRequires:  libtool

%description
An automatic display manager which automatically starts an X session at
system boot. It is meant for devices like smartphones, but can be used
on a regular computer as well, if the security implications are acceptable.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%{_mandir}/man8/%{name}.8.gz


%changelog
* Sun Feb 14 2010 Sebastian Dziallas <sebastian@when.com> - 0.6-2
- fix issue with DSO linking thanks to Mathieu Bridon

* Thu Jan 28 2010 Sebastian Dziallas <sebastian@when.com> - 0.6-1
- initial packaging
