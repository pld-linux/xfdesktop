Summary:	Desktop manager for the Xfce Desktop Environment
Summary(pl.UTF-8):	Zarządca pulpitu dla środowiska Xfce
Name:		xfdesktop
Version:	4.20.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/xfce/xfdesktop/4.20/%{name}-%{version}.tar.bz2
# Source0-md5:	b845397fed5e555fa8dce4b189365dbc
URL:		https://www.xfce.org/projects/xfdesktop
BuildRequires:	Thunar-devel >= 4.20.0
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.84
BuildRequires:	exo-devel >= 0.11.0
BuildRequires:	garcon-devel >= 0.6.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.72.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libnotify-devel >= 0.4.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libwnck-devel >= 3.14
BuildRequires:	libxfce4ui-devel >= 4.20.0
BuildRequires:	libxfce4util-devel >= 4.20.0
BuildRequires:	libxfce4windowing-devel >= 4.20.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 2.000
BuildRequires:	xfce4-dev-tools >= 4.20.0
BuildRequires:	xfconf-devel >= 4.20.0
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	yaml-devel >= 0.2.5
Requires:	Thunar-libs >= 4.20.0
Requires:	dbus-glib >= 0.84
Requires:	exo >= 0.12.0
Requires:	garcon >= 0.6.0
Requires:	glib2 >= 1:2.72.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	libxfce4ui >= 4.20.0
Requires:	libxfce4util >= 4.20.0
Requires:	xfce4-dirs >= 4.6
Requires:	xfconf >= 4.20.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfdesktop contain a desktop manager for the Xfce Desktop Environment.

%description -l pl.UTF-8
xfdesktop zawiera zarządcę pulpitu dla środowiska Xfce.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--enable-desktop-icons \
	--enable-desktop-menu \
	--enable-file-icons \
	--enable-thunarx

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unify dir name (verify first that target doesn't exist)
[ ! -e $RPM_BUILD_ROOT%{_localedir}/fa ] || exit 1
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{fa_IR,fa}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}
# just a copy of ur (.po files differ only by trailing junk)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK
# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/xfdesktop
%attr(755,root,root) %{_bindir}/xfdesktop-settings
%{_mandir}/man1/xfdesktop.1*
%{_desktopdir}/xfce-backdrop-settings.desktop
%{_pixmapsdir}/xfce4_xicon*.png
%{_pixmapsdir}/xfdesktop
%{_iconsdir}/hicolor/*x*/apps/org.xfce.xfdesktop.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.xfdesktop.svg
%dir %{_datadir}/backgrounds/xfce
%{_datadir}/backgrounds/xfce/xfce-blue.jpg
%{_datadir}/backgrounds/xfce/xfce-cp-dark.svg
%{_datadir}/backgrounds/xfce/xfce-light.svg
%{_datadir}/backgrounds/xfce/xfce-mouserace.svg
%{_datadir}/backgrounds/xfce/xfce-stripes.svg
%{_datadir}/backgrounds/xfce/xfce-teal.svg
%{_datadir}/backgrounds/xfce/xfce-verticals.svg
%{_datadir}/backgrounds/xfce/xfce-x.svg
%{_datadir}/backgrounds/xfce/xfce-flower.svg
%{_datadir}/backgrounds/xfce/xfce-leaves.svg
%{_datadir}/backgrounds/xfce/xfce-shapes.svg
