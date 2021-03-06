%define __python_module requests
%define __python_version 36
%define __python_distdir %(%{__python36} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:           python-idna
Version:        2.6
Release:        2%{?dist}
Summary:         Internationalized Domain Names for Python (IDNA 2008 and UTS #46)

License:        MIT
URL:            https://pypi.python.org/pypi/idna
Source0:        https://github.com/kjd/idna/archive/v%{version}.tar.gz

BuildArch:      noarch

%description
Support for the Internationalised Domain Names in Applications (IDNA) protocol as specified in RFC 5891. This is the latest version of the protocol and is sometimes referred to as "IDNA 2008".

This library also provides support for Unicode Technical Standard 46, Unicode IDNA Compatibility Processing.

This acts as a suitable replacement for the "encodings.idna" module that comes with the Python standard library, but only supports the old, deprecated IDNA specification (RFC 3490).


%prep
%setup -q -n idna-%{version}


%build
%{__python36} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python36} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-lib %{__python_distdir}

 
%files
%doc README.rst HISTORY.rst
%{__python_distdir}/idna/*.py
%{__python_distdir}/*.egg-info
%exclude %{__python_distdir}/idna/__pycache__

%changelog
* Thu Nov 09 2017 Marwan Rabbâa <marwan.rabbaa@pandacraft.com> - 2.6
- Package creation for production usage on amzn 2017.03
