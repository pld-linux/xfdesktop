Summary:	Desktop manager for the XFce Desktop Environment
Summary(pl):	Zarz±dca pulpitu dla ¶rodowiska XFce
Name:		xfdesktop
Version:	4.0.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	eef02de6de0ac2b8343f4ce2c2f8cf12
URL:		http://www.xfce.org/
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= %{version}
Requires:	libxfce4mcs >= %{version}
Requires:	libxfcegui4 >= %{version}
Requires:	xfce-mcs-manager >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfdesktop contain a desktop manager for the XFce Desktop Environment.

%description -l pl
xfdesktop zawiera zarz±dcê pulpitu dla ¶rodowiska XFce.

%prep
%setup -q

%build
#rm -f missing
glib-gettextize --copy --force
intltoolize --copy --force
cp -f /usr/share/automake/config.sub .
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
%lang(az) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.az
%lang(ca) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.ca
%lang(de) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.de
%lang(fr) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.fr
%lang(hu) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.hu
%lang(nl) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.nl
%lang(ta) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.ta
%lang(tr) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.tr
%lang(vi) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.vi
%lang(zh_CN) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.zh_CN
%lang(zh_TW) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.zh_TW
%{_datadir}/xfce4/backdrops
%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*
