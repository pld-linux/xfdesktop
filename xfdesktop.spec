Summary: 	Desktop manager for the XFce Desktop Environment
Name: 		xfdesktop
Version: 	3.90.0
Release: 	0.1
License:	GPL
URL: 		http://www.xfce.org/
Source0: 	http://belnet.dl.sourceforge.net/sourceforge/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	89b8a261b5f0d73d88bae8d504fec783
Group: 		X11/Applications
Requires:	libxfce4mcs >= 0.0.4
Requires:	libxfcegui4 >= 0.0.17
BuildRequires:	libxfce4mcs-devel >= 0.0.4
BuildRequires: 	libxfcegui4-devel >= 0.0.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfdesktop contain a desktop manager for the XFce Desktop Environment

%prep
%setup -q

%build
rm -f missing
glib-gettextize --copy --force
intltoolize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog NEWS INSTALL COPYING AUTHORS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%{_libdir}/xfce4/mcs-plugins/*.la
%{_libdir}/xfce4/mcs-plugins/*.a
%{_sysconfdir}/xfce4/
%{_datadir}/locale/
%{_datadir}/xfce4/
