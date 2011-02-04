Summary:	Desktop manager for the Xfce Desktop Environment
Summary(pl.UTF-8):	Zarządca pulpitu dla środowiska Xfce
Name:		xfdesktop
Version:	4.6.2
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	e800ea9fee7a5c5eaf2ae96e23a83e3a
Patch0:		%{name}-generic-menu.patch
URL:		http://www.xfce.org/projects/xfdesktop/
BuildRequires:	Thunar-devel >= 1.0.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	exo-devel >= 0.3.100
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.12.0
BuildRequires:	libxfce4menu-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.6.0
BuildRequires:	xfce4-panel-devel >= %{version}
BuildRequires:	xfconf-devel >= %{version}
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-dirs >= 4.6
Requires:	xfce4-panel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfdesktop contain a desktop manager for the Xfce Desktop Environment.

%description -l pl.UTF-8
xfdesktop zawiera zarządcę pulpitu dla środowiska Xfce.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__aclocal}
%{__intltoolize}
%{__autoheader}
%{__automake}
%{__aclocal}
%configure \
	--enable-desktop-icons \
	--enable-desktop-menu \
	--enable-exo \
	--enable-file-icons \
	--enable-panel-plugin \
	--enable-thunarx

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/{panel-plugins,modules}/*.{la,a}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

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
%attr(755,root,root) %{_bindir}/xfce4-popup-menu
%attr(755,root,root) %{_bindir}/xfdesktop
%attr(755,root,root) %{_bindir}/xfdesktop-settings
%dir %{_libdir}/xfce4/modules
%attr(755,root,root) %{_libdir}/xfce4/modules/xfce4_desktop_menu.so
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-menu-plugin

%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*.png
%lang(da) %{_datadir}/xfce4/doc/da/*.html
%lang(fr) %{_datadir}/xfce4/doc/fr/*.html
%lang(fr) %{_datadir}/xfce4/doc/fr/images/*.png
%lang(it) %{_datadir}/xfce4/doc/it/*.html
%lang(it) %{_datadir}/xfce4/doc/it/images/*.png
%lang(ja) %{_datadir}/xfce4/doc/ja/*.html
%lang(ja) %{_datadir}/xfce4/doc/ja/images/*.png
%{_mandir}/man1/*.1*

%{_sysconfdir}/xdg/menus
%{_desktopdir}/*.desktop
%{_datadir}/desktop-directories/*
%{_datadir}/xfce4/backdrops
%{_datadir}/xfce4/panel-plugins/*
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/*/apps/*
