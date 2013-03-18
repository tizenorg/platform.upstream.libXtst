Name:           libXtst
Version:        1.2.1
Release:        0
License:        MIT
Summary:        Xlib-based client API for the XTEST and RECORD extensions
Url:            http://xorg.freedesktop.org/
Group:          Graphics/X Window System

Source:         %{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(recordproto) >= 1.13.99.1
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext) >= 1.0.99.4
BuildRequires:  pkgconfig(xextproto) >= 7.0.99.3
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xorg-macros) >= 1.12

%description
The XTEST extension is a minimal set of client and server extensions
required to completely test the X11 server with no user intervention.
This extension is not intended to support general journaling and
playback of user actions.

The RECORD extension supports the recording and reporting of all core
X protocol and arbitrary X extension protocol.

%package devel
Summary:        Development files for the X11 XTEST and RECORD extensions
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
The XTEST extension is a minimal set of client and server extensions
required to completely test the X11 server with no user intervention.
This extension is not intended to support general journaling and
playback of user actions.

The RECORD extension supports the recording and reporting of all core
X protocol and arbitrary X extension protocol.

This package contains the development headers for the library found
in %{name}.

%prep
%setup -q

%build
%configure --docdir=%_docdir/%{name} --disable-static
make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}

%remove_docs

%post  -p /sbin/ldconfig

%postun  -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%{_libdir}/libXtst.so.6*

%files devel
%defattr(-,root,root)
%{_includedir}/X11/*
%{_libdir}/libXtst.so
%{_libdir}/pkgconfig/xtst.pc

%changelog
