# 
# TODO:
# - %{_libdir}/xfce4/modules have to belong somewhere (but where?)
#
%define		snap 20040617
#
Summary:	Desktop manager for the XFce Desktop Environment
Summary(pl):	Zarz�dca pulpitu dla �rodowiska XFce
Name:		xfdesktop
Version:	4.1.0
Release:	0.%{snap}.1
License:	GPL
Group:		X11/Applications
Source0:	%{name}-snap-%{snap}.tar.bz2
# Source0-md5:	7070804f081dce2c877af2b10437e22d
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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
xfdesktop zawiera zarz�dc� pulpitu dla �rodowiska XFce.

%prep
%setup -q -n %{name}

%build
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
%{_datadir}/xfce4/doc/C
%lang(fr) %{_datadir}/xfce4/doc/fr

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/*/*.so

%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml
%lang(az) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.az
%lang(ca) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.ca
%lang(de) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.de
%lang(es) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.es
%lang(eu) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.eu
%lang(fa_IR) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.fa_IR
%lang(fr) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.fr
%lang(hu) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.hu
%lang(ms) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.ms
%lang(nl) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.nl
%lang(ta) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.ta
%lang(tr) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.tr
%lang(vi) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.vi
%lang(zh_CN) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.zh_CN
%lang(zh_TW) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.zh_TW

%{_sysconfdir}/xfce4/xfce-registered-categories.xml
%{_desktopdir}/*.desktop
%{_datadir}/xfce4/backdrops
%{_datadir}/pixmaps/*
%{_iconsdir}/hicolor/*/apps/*
