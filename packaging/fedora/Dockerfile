FROM fedora:43
RUN dnf install -y perl-Expect perl-File-chdir perl-File-Find-Rule perl-Inline-Python perl-JSON perl-Net-IP perl-TOML-Parser perl-YAML perl-XML-Parser grc automake
RUN dnf install -y fedora-packager rpmdevtools gcc 
WORKDIR /root
RUN rpmdev-setuptree
WORKDIR /root/rpmbuild
RUN rpmdev-newspec --macros workflow-automation-engine.spec
ENTRYPOINT ["cat", "workflow-automation-engine.spec"]
