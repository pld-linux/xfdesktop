Summary:	Desktop manager for the XFce Desktop Environment
Summary(pl):	Zarz±dca pulpitu dla ¶rodowiska XFce
Name:		xfdesktop
Version:	3.99.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://linux.imp.mx/xfce4/rc2/xfce4-rc2/src/%{name}-%{version}.tar.gz
# Source0-md5:	d9ae203f5f23abe17feea1181b9aca08
URL:		http://www.xfce.org/
BuildRequires:	intltool
BuildRequires:	libxfce4mcs-devel >= 3.99.2
BuildRequires:	libxfcegui4-devel >= 3.99.2
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= 3.99.2
Requires:	libxfce4mcs >= 3.99.2
Requires:	libxfcegui4 >= 3.99.2
Requires:	xfce-mcs-manager >= 3.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfdesktop contain a desktop manager for the XFce Desktop Environment.

%description -l pl
xfdesktop zawiera zarz±dcê pulpitu dla ¶rodowiska XFce.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml
%{_datadir}/xfce4/backdrops
%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*
