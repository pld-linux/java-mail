%bcond_without  javadoc         # don't build javadoc
#
%include	/usr/lib/rpm/macros.java
#
%define	srcname	mail
Summary:	JavaMail - Java mail system
Summary(pl.UTF-8):	JavaMail - system pocztowy w Javie
Name:		java-mail
Version:	1.4.1
Release:	6
License:	CDDL
Group:		Libraries/Java
Source0:	https://maven-repository.dev.java.net/nonav/repository/javax.mail/jars/mail-%{version}-sources.jar
# Source0-md5:	e5517da355c865a6451c451e45ccbba1
URL:		http://java.sun.com/products/javamail/
BuildRequires:	java(jaf)
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java(jaf)
Requires:	jpackage-utils
Provides:	java(javamail) = %{version}-%{release}
Obsoletes:	javamail
Obsoletes:	java(javamail)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The JavaMail(TM) API provides a set of abstract classes that model a
mail system. The API provides a platform independent and protocol
independent framework to build Java technology-based mail and
messaging applications.

%description -l pl.UTF-8
API JavaMail(TM) daje zestaw klas abstrakcyjnych tworzących system
pocztowy. API daje niezależne od platformy i protokołu środowisko do
tworzenia aplikacji pocztowych i komunikacyjnych w oparciu o Javę.

%package javadoc
Summary:	Online manual for java-mail
Summary(pl.UTF-8):	Dokumentacja online do java-mail
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for java-mail.

%description javadoc -l pl.UTF-8
Dokumentacja do java-mail.

%description javadoc -l fr.UTF-8
Javadoc pour java-mail.

%prep
%setup -qc

%build
CLASSPATH=$(build-classpath activation)

install -d build
%javac -classpath $CLASSPATH -source 1.4 -target 1.4 -d build $(find -name '*.java')

%if %{with javadoc}
%javadoc -d apidocs \
	%{?with_java_sun:com.sun.mail} \
	$(find com/sun/mail -name '*.java') 
%endif

%jar -cf %{srcname}-%{version}.jar -C build .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/javamail-%{version}.jar

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%{_javadir}/javamail-%{version}.jar
%{_javadir}/%{srcname}-%{version}.jar
%{_javadir}/%{srcname}.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
