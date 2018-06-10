Summary:	Desktop manager for the Xfce Desktop Environment
Summary(pl.UTF-8):	Zarządca pulpitu dla środowiska Xfce
Name:		xfdesktop
Version:	4.13.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/xfdesktop/4.13/%{name}-%{version}.tar.bz2
# Source0-md5:	9e7d04e79053cf9ec077f55425f234c6
URL:		http://www.xfce.org/projects/xfdesktop
Patch0:		thunarx-3.patch
BuildRequires:	Thunar-devel >= 1.8.0
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.84
BuildRequires:	exo-devel >= 0.12.0
BuildRequires:	garcon-devel >= 0.6.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.30.0
BuildRequires:	gtk+3-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libnotify-devel >= 0.4.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libwnck-devel
BuildRequires:	libxfce4ui-devel >= 4.13.0
BuildRequires:	libxfce4util-devel >= 4.12.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	xfconf-devel >= 4.12.1
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	Thunar-libs >= 1.8.0
Requires:	dbus-glib >= 0.84
Requires:	exo >= 0.12.0
Requires:	garcon >= 0.6.0
Requires:	glib2 >= 1:2.30.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	libxfce4ui >= 4.13.0
Requires:	libxfce4util >= 4.12.0
Requires:	xfce4-dirs >= 4.6
Requires:	xfconf >= 4.12.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfdesktop contain a desktop manager for the Xfce Desktop Environment.

%description -l pl.UTF-8
xfdesktop zawiera zarządcę pulpitu dla środowiska Xfce.

%prep
%setup -q
%patch0 -p1


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
[ ! -e $RPM_BUILD_ROOT%{_datadir}/locale/fa ] || exit 1
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{fa_IR,fa}
# just a copy of ur (.po files differ only by trailing junk)
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

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
%attr(755,root,root) %{_bindir}/xfdesktop
%attr(755,root,root) %{_bindir}/xfdesktop-settings
%{_mandir}/man1/xfdesktop.1*
%{_desktopdir}/xfce-backdrop-settings.desktop
%{_pixmapsdir}/xfce4_xicon*.png
%{_pixmapsdir}/xfdesktop
%{_iconsdir}/hicolor/*/apps/xfce4-backdrop.*
%{_iconsdir}/hicolor/*/apps/xfce4-menueditor.*
%dir %{_datadir}/backgrounds/xfce
%{_datadir}/backgrounds/xfce/xfce-blue.jpg
%{_datadir}/backgrounds/xfce/xfce-teal.jpg
