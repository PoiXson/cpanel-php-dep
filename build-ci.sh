# sh build-ci.sh  --dl-path=/home/pxn/www/dl/cpanel-php-dep  --yum-path=/home/pxn/www/yum/extras-testing/noarch


# load build_utils.sh script
if [ -e build_utils.sh ]; then
	source ./build_utils.sh
elif [ -e /usr/local/bin/pxn/build_utils.sh ]; then
	source /usr/local/bin/pxn/build_utils.sh
else
	wget https://raw.githubusercontent.com/PoiXson/shellscripts/master/pxn/build_utils.sh \
		|| exit 1
	source ./build_utils.sh
fi


NAME="cpanel-php-dep"
NAME4="cpanel-php54-dep"
NAME5="cpanel-php55-dep"
NAME6="cpanel-php56-dep"
[ -z "${WORKSPACE}" ] && WORKSPACE=`pwd`
rm -vf "${WORKSPACE}/${NAME}"-*.noarch.rpm


title "Build.."
( cd "${WORKSPACE}/" && sh build-rpm.sh --build-number ${BUILD_NUMBER} ) || exit 1


title "Deploy.."
cp -fv "${WORKSPACE}/${NAME4}"-*.noarch.rpm "${DL_PATH}/" || exit 1
cp -fv "${WORKSPACE}/${NAME5}"-*.noarch.rpm "${DL_PATH}/" || exit 1
cp -fv "${WORKSPACE}/${NAME6}"-*.noarch.rpm "${DL_PATH}/" || exit 1
# php 5.4
latest_version "${DL_PATH}/${NAME4}-*.noarch.rpm"         || exit 1
echo "Latest version: "${LATEST_FILE}
ln -fs "${LATEST_FILE}" "${YUM_PATH}/${NAME4}.noarch.rpm" || exit 1
# php 5.5
latest_version "${DL_PATH}/${NAME5}-*.noarch.rpm"         || exit 1
echo "Latest version: "${LATEST_FILE}
ln -fs "${LATEST_FILE}" "${YUM_PATH}/${NAME5}.noarch.rpm" || exit 1
# php 5.6
latest_version "${DL_PATH}/${NAME6}-*.noarch.rpm"         || exit 1
echo "Latest version: "${LATEST_FILE}
ln -fs "${LATEST_FILE}" "${YUM_PATH}/${NAME6}.noarch.rpm" || exit 1

