Summary:	XroadMaker - printed circuit board designer
Summary(pl):	XroadMaker - program do projektowania p³ytek drukowanych
Name:		xroadmaker
Version:	0.5.6
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/xroadmaker/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://xroadmaker.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	gnome-libs-devel >= 1.0.57
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XRoadMaker is a gnome printed circuit board designer.

%description -l pl
XRoadMaker jest narzêdziem do projektowania p³ytek drukowanych dla
GNOME.

%prep
%setup -q
%patch -p1

%build
#CXXFLAGS="-Wall %{rpmcflags}"

%{__autoconf}
%configure
(cd src; cp -f support_custom.c support.c;cp -f support_custom.h support.h)
%{__make}
#RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HISTORY README USAGE
%attr(755,root,root) %{_bindir}/xroadmaker
%dir %{_datadir}/%{name}
%attr(644,root,root) %{_datadir}/%{name}/config
%attr(644,root,root) %{_datadir}/%{name}/libs

%dir %{_pixmapsdir}/%{name}
%attr(644,root,root) %{_pixmapsdir}/%{name}/*.xpm
