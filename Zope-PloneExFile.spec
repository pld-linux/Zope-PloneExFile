%define		zope_subname	PloneExFile
Summary:	A Plone content type with an attachment
Summary(pl):	Typ Plone z za³±cznikami
Name:		Zope-%{zope_subname}
Version:	3.01
Release:	1
License:	ZPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/ingeniweb/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	4714bc9571ea2e512f74663619b84a36
URL:		http://sourceforge.net/projects/ingeniweb/
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-ZAttachmentAttribute >= 2.0
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Plone content type with an attachment.

%description -l pl
Typ Plone z za³±cznikami.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af Extensions i18n skins website *.py *.txt \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc ABOUT CHANGES CREDITS ChangeLog README.txt doc/*
%{_datadir}/%{name}
