Summary:	Desktop manager for the Xfce Desktop Environment
Summary(pl.UTF-8):	Zarządca pulpitu dla środowiska Xfce
Name:		xfdesktop
Version:	4.10.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/xfdesktop/4.10/%{name}-%{version}.tar.bz2
# Source0-md5:	d5f6fb9fdde3ddff5804b2a251892936
URL:		http://www.xfce.org/projects/xfdesktop
BuildRequires:	Thunar-devel >= 1.4.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	exo-devel >= 0.8.0
BuildRequires:	garcon-devel >= 0.1.3
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libnotify-devel >= 0.4.0
BuildRequires:	libtool
BuildRequires:	libwnck2-devel >= 2.22.0
BuildRequires:	libxfce4ui-devel >= 4.10.0
BuildRequires:	libxfce4util-devel >= 4.10.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.10.0
BuildRequires:	xfconf-devel >= 4.10.0
Requires:	garcon >= 0.2.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-dirs >= 4.6
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
	--enable-exo \
	--enable-file-icons \
	--enable-thunarx

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_mandir}/man1/*.1*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/*/apps/*
%dir %{_datadir}/backgrounds/xfce
%{_datadir}/backgrounds/xfce/xfce-blue.jpg
