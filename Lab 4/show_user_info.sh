#!/bin/sh

echo "User: $(whoami)"
echo ""

echo "User ID:"
id
echo ""

echo "Home catalogue:"
ls -la ~
echo ""

echo "User groups:"
groups
echo ""

case "$(whoami)" in
  may)
    echo "Hey May"
    ;;
  lukasz)
    echo "Hey Lukasz"
    ;;
  hajdi)
    echo "Hey Hajdi"
    ;;
  *)
    echo "Unknown user"
    ;;
esac