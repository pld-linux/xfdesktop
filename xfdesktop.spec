 
# - %{_libdir}/xfce4/modules have to belong somewhere (but where?)
# belongs to libxfcegui4
Summary:	Desktop manager for the XFce Desktop Environment
Summary(pl):	Zarz±dca pulpitu dla ¶rodowiska XFce
Name:		xfdesktop
Version:	4.1.99.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e143f8eb9f6c22230040550e26af8ac6
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= 4.1.0
BuildRequires:	xfce4-panel-devel >= %{version}
BuildRequires:	libxml2-devel >= 2.4.0
Requires:	gtk+2 >= 2.2.0
Requires:	libxfce4mcs >= %{version}
Requires:	libxfcegui4 >= %{version}
Requires:	xfce4-panel >= %{version}
Requires:	xfce-mcs-manager >= 4.1.0
Requires:	libxml2 >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfdesktop contain a desktop manager for the XFce Desktop Environment.

%description -l pl
xfdesktop zawiera zarz±dcê pulpitu dla ¶rodowiska XFce.

%prep
%setup -q
%patch0 -p1

mv -f po/{pt_PT,pt}.po
mv -f menu.xml.fa_IR menu.xml.fa

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/{mcs-plugins,panel-plugins,modules}/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
%lang(it) %{_datadir}/xfce4/doc/it/*
%{_mandir}/man1/*.1*

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/*/*.so

%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml
%lang(az) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.az
%lang(ca) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.ca
%lang(de) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.de
%lang(es) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.es
%lang(et) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.et
%lang(eu) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.eu
%lang(fa) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.fa
%lang(fr) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.fr
%lang(he) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.he
%lang(hu) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.hu
%lang(ms) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.ms
%lang(nl) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.nl
%lang(ro) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.ro
%lang(ru) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.ru
%lang(sk) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.sk
%lang(ta) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.ta
%lang(tr) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.tr
%lang(vi) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.vi
%lang(zh_CN) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.zh_CN
%lang(zh_TW) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.zh_TW

%{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml
%lang(nl) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.nl
%lang(zh_TW) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.zh_TW
%{_desktopdir}/*.desktop
%{_datadir}/xfce4/backdrops
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor/*/apps/*
