Summary:	Desktop manager for the Xfce Desktop Environment
Summary(pl):	Zarz±dca pulpitu dla ¶rodowiska Xfce
Name:		xfdesktop
Version:	4.4.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	a1c93d228924b5daf151f698114021d3
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	Thunar-devel >= 0.8.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.8.20
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libexo-devel >= 0.3.2
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	xfce4-dev-tools >= %{version}
BuildRequires:	xfce4-panel-devel >= %{version}
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	xdg-menus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfdesktop contain a desktop manager for the Xfce Desktop Environment.

%description -l pl
xfdesktop zawiera zarz±dcê pulpitu dla ¶rodowiska Xfce.

%prep
%setup -q
%patch0 -p1

mv -f po/{pt_PT,pt}.po
mv -f po/{nb_NO,nb}.po

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-desktop-icons \
	--enable-desktop-menu \
	--enable-exo \
	--enable-file-icons \
	--enable-panel-plugin \
	--enable-menueditor \
	--enable-thunarx

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/{mcs-plugins,panel-plugins,modules}/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%attr(755,root,root) %{_libdir}/xfce4/modules/*.so
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-menu-plugin
%dir %{_datadir}/xfce4-menueditor
%{_datadir}/xfce4-menueditor/xfce4-menueditor.ui
%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
%{_mandir}/man1/*.1*

%dir %{_sysconfdir}/xdg/xfce4/desktop
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml
%lang(ca) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.ca
%lang(cs) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.cs
%lang(da) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.da
%lang(de) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.de
%lang(el) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.el
%lang(es) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.es
%lang(et) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.et
%lang(eu) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.eu
%lang(fi) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.fi
%lang(fr) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.fr
%lang(he) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.he
%lang(hu) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.hu
%lang(ja) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.ja
%lang(ko) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.ko
%lang(nl) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.nl
%lang(pl) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.pl
%lang(pt_BR) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.pt_BR
%lang(ro) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.ro
%lang(ru) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.ru
%lang(sk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.sk
%lang(sv) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.sv
%lang(uk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.uk
%lang(vi) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.vi
%lang(zh_TW) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/xfce4/desktop/menu.xml.zh_TW

%{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml
%lang(ca) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.ca
%lang(cs) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.cs
%lang(de) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.de
%lang(el) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.el
%lang(es) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.es
%lang(eu) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.eu
%lang(fi) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.fi
%lang(fr) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.fr
%lang(he) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.he
%lang(hu) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.hu
%lang(ja) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.ja
%lang(nl) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.nl
%lang(pl) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.pl
%lang(pt_BR) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.pt_BR
%lang(ro) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.ro
%lang(ru) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.ru
%lang(sk) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.sk
%lang(sv) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.sv
%lang(zh_CN) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.zh_CN
%lang(zh_TW) %{_sysconfdir}/xdg/xfce4/desktop/xfce-registered-categories.xml.zh_TW
%{_desktopdir}/*.desktop
%{_datadir}/xfce4/backdrops
%{_datadir}/xfce4/panel-plugins/*
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/*/apps/*
