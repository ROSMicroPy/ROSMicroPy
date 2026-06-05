#!/bin/sh
set -eu

ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
OUT="$ROOT/web-loader/firmware"
RELEASE="$ROOT/release"

mkdir -p "$OUT"

cp "$RELEASE/rmp_core_generic.bin" "$OUT/rmp_core_generic.bin"
cp "$RELEASE/rmp_core_generic_bootloader.bin" "$OUT/rmp_core_generic_bootloader.bin"
cp "$RELEASE/rmp_core_generic_partition-table.bin" "$OUT/rmp_core_generic_partition-table.bin"

cp "$RELEASE/rmp_core_s3.bin" "$OUT/rmp_core_s3.bin"
cp "$RELEASE/rmp_core_s3_bootloader.bin" "$OUT/rmp_core_s3_bootloader.bin"
cp "$RELEASE/rmp_core_s3_partition-table.bin" "$OUT/rmp_core_s3_partition-table.bin"

echo "Synced ROSMicroPy Core firmware into $OUT"
