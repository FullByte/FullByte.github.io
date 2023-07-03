# Tags

Replace the tags "key1" with "key2" for all the resource

```ps1
$replacedTags= @{"key1"="value1"; "key2"="value2"}
$resourcelist= Get-AzResource
foreach($item in $resourcelist){
    Update-Aztag -ResourceId $item.ResourceId -Tag $replacedTags -Operation Replace
}
```

Replace a specific tag "key3" with new "value3"

```ps1
$replacedTags= @{"key3"="value3"}
$resourcelist= Get-AzResource

foreach($item in $resourcelist){
    
    $existtags=(Get-AzTag -ResourceId $item.ResourceId)
    if(($existtags.Properties.TagsProperty.Values -contains 'value1') -and ( $existtags.Properties.TagsProperty.Keys -contains 'key1'))
    {
        Update-Aztag -ResourceId $item.ResourceId -Tag $replacedTags -Operation Replace
    }
}
```

Merge specific tags "key2" and "key3"

```ps1
$mergedTags=@{"key2"="value2"; "key3"="value3"}
$resourcelist= Get-AzResource
foreach($item in $resourcelist){
    
    $existtags=(Get-AzTag -ResourceId $item.ResourceId)
    if(($existtags.Properties.TagsProperty.Values -contains 'key1') -and ( $existtags.Properties.TagsProperty.Keys -contains 'value1'))
    {
        Update-AzTag -ResourceId $item.ResourceId -Tag $mergedTags -Operation Merge
    }
}
```
