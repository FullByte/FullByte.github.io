# Squoosh

Make images smaller using best-in-class codecs, right in the browser.

| What          | Where                                         |
|---------------|-----------------------------------------------|
| Official Page | <https://squoosh.app/>                        |
| Source        | <https://github.com/GoogleChromeLabs/squoosh> |
| Install       | `npm i -g @squoosh/cli`                         |

## JPEG Example

Simple example to compress an JPEG image

``` sh
squoosh-cli --mozjpeg '{quality:50}' image.png -d output
```

Compress an JPEG image with more parameters (default):

``` sh
squoosh-cli --mozjpeg \
'{ 
   "quality":75, 
   "baseline":false, 
   "arithmetic":false, 
   "progressive":true, 
   "op timize_coding":true, 
   "smoothing":0, 
   "color_space":3, 
   "quant_table":3, 
   "trellis_multipass":false, 
   "trel lis_opt_zero":false, 
   "trellis_opt_table":false, 
   "trellis_loops":1, 
   "auto_subsample":true, 
   "chroma_sub sample":2, 
   "separate_chroma_quality":false, 
   "chroma_quality":75 
}' \
~/path/to/image.jpg -d output ./*
```

## PNG Example

Simple example to compress an PNG image

``` sh
squoosh-cli --oxipng '{level:2}' image.png -d output
```

## WEBP Example

Compress an webp image with more parameters (default):

``` sh
squoosh-cli --webp \
'{ 
    quality: 75,
    target_size: 0,
    target_PSNR: 0,
    method: 4,
    sns_strength: 50,
    filter_strength: 60,
    filter_sharpness: 0,
    filter_type: 1,
    partitions: 0,
    segments: 4,
    pass: 1,
    show_compressed: 0,
    preprocessing: 0,
    autofilter: 0,
    partition_limit: 0,
    alpha_compression: 1,
    alpha_filtering: 1,
    alpha_quality: 100,
    lossless: 0,
    exact: 0,
    image_hint: 0,
    emulate_jpeg_size: 0,
    thread_level: 0,
    low_memory: 0,
    near_lossless: 100,
    use_delta_palette: 0,
    use_sharp_yuv: 0
    }' \
~/path/to/image.jpg -d output ./*
```
