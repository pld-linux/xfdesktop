Summary:	Desktop manager for the XFce Desktop Environment
Summary(pl):	Zarz�dca pulpitu dla �rodowiska XFce
Name:		xfdesktop
Version:	4.0.6
Release:	1
License:	GPL
Group:		X11/Applications
#Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
Source0:	http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	8f7a87ada82eaa60fb37998553787002
Patch0:		%{name}-menu.patch
Patch1:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	startup-notification-devel
BuildRequires:	xfce-mcs-manager-devel >= %{version}
Requires(post):	vfmg >= 0.9.16-2
Requires:	libxfce4mcs >= %{version}
Requires:	libxfcegui4 >= %{version}
Requires:	libxml2 >= 2.4.0
Requires:	startup-notification
Requires:	vfmg > 0.9.16-2
Requires:	xfce-mcs-manager >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfdesktop contain a desktop manager for the XFce Desktop Environment.

%description -l pl
xfdesktop zawiera zarz�dc� pulpitu dla �rodowiska XFce.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{fa_IR,fa}.po
mv -f po/{no,nb}.po
mv -f po/{pt_PT,pt}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{_sysconfdir}/xfce4/menu2.xml
rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
vfmg -i -f -x -c -u -m xfce4 > %{_sysconfdir}/xfce4/menu2.xml 2>/dev/null

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu2.xml
%lang(az) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.az
%lang(ca) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.ca
%lang(de) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.de
%lang(fr) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.fr
%lang(hu) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.hu
%lang(it) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.it
%lang(nl) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.nl
%lang(pl) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.pl
%lang(ta) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.ta
%lang(tr) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.tr
%lang(vi) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.vi
%lang(zh_CN) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.zh_CN
%lang(zh_TW) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/menu.xml.zh_TW
%{_datadir}/xfce4/backdrops
%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*.html
%lang(fr) %{_datadir}/xfce4/doc/fr/images/*
