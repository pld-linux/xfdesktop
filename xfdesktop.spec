Summary:	Desktop manager for the Xfce Desktop Environment
Summary(pl.UTF-8):	Zarządca pulpitu dla środowiska Xfce
Name:		xfdesktop
Version:	4.7.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce/4.8pre1/src/%{name}-%{version}.tar.bz2
# Source0-md5:	88d10a7775f65a007639f921c5c8f13a
Patch0:		%{name}-generic-menu.patch
URL:		http://www.xfce.org/projects/xfdesktop/
BuildRequires:	Thunar-devel >= 1.0.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	exo-devel >= 0.5.4
BuildRequires:	garcon-devel >= 0.1.3
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.12.0
#BuildRequires:	libxfce4ui-devel >= %{version}
BuildRequires:	libxfce4ui-devel >= 4.7.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.6.0
#BuildRequires:	xfce4-panel-devel >= %{version}
#BuildRequires:	xfconf-devel >= %{version}
BuildRequires:	xfce4-panel-devel >= 4.7.0
BuildRequires:	xfconf-devel >= 4.7.0
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	garcon >= 0.1.2
Requires:	xfce4-dirs >= 4.6
#Requires:	xfce4-panel >= %{version}
Requires:	xfce4-panel >= 4.7.0
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

%if 0
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*.png
%lang(da) %{_datadir}/xfce4/doc/da/*.html
%lang(fr) %{_datadir}/xfce4/doc/fr/*.html
%lang(fr) %{_datadir}/xfce4/doc/fr/images/*.png
%lang(it) %{_datadir}/xfce4/doc/it/*.html
%lang(it) %{_datadir}/xfce4/doc/it/images/*.png
%lang(ja) %{_datadir}/xfce4/doc/ja/*.html
%lang(ja) %{_datadir}/xfce4/doc/ja/images/*.png
%endif
%{_mandir}/man1/*.1*

%{_desktopdir}/*.desktop
%{_datadir}/xfce4/backdrops
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/*/apps/*
