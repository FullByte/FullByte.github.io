# Policies

## Add multiple tags to resource if missing

Create a new custom policy definition and add the following information:

- Definition location: This policy works well on subscription level
- Name: Add multiple tags to resource if missing
- Description: Adds multiple tags with its value from the parent resource group when any resource missing this tag is created or updated. Existing resources can be remediated by triggering a remediation task. If the tag exists with a different value it will not be changed.
- Category: I suggest to create a new category e.g. called "custom" or similar to be able to easily find own policy definitions later
- Policy Rule: Add the json from below (Adjust the number of tags to inherit if needed):

``` json
{
  "properties": {
    "displayName": "Add multiple tags to resource if missing",
    "policyType": "Custom",
    "mode": "Indexed",
    "description": "Adds multiple tags with its value from the parent resource group when any resource missing this tag is created or updated. Existing resources can be remediated by triggering a remediation task. If the tag exists with a different value it will not be changed.",
    "parameters": {
      "tagName1": {
        "type": "String",
        "metadata": {
          "displayName": "First Tag Name",
          "description": "Name of the tag, such as 'environment'"
        }
      },
      "tagName2": {
        "type": "String",
        "metadata": {
          "displayName": "Second Tag Name",
          "description": "Name of the tag, such as 'environment'"
        }
      },
      "tagName3": {
        "type": "String",
        "metadata": {
          "displayName": "Third Tag Name",
          "description": "Name of the tag, such as 'environment'"
        }
      },
      "tagName4": {
        "type": "String",
        "metadata": {
          "displayName": "Forth Tag Name",
          "description": "Name of the tag, such as 'environment'"
        }
      },
      "tagName5": {
        "type": "String",
        "metadata": {
          "displayName": "Fifth Tag Name",
          "description": "Name of the tag, such as 'environment'"
        }
      },
      "tagName6": {
        "type": "String",
        "metadata": {
          "displayName": "Sixth Tag Name",
          "description": "Name of the tag, such as 'environment'"
        }
      },
      "tagName7": {
        "type": "String",
        "metadata": {
          "displayName": "Seventh Tag Name",
          "description": "Name of the tag, such as 'environment'"
        }
      },
      "tagName8": {
        "type": "String",
        "metadata": {
          "displayName": "Eighth Tag Name",
          "description": "Name of the tag, such as 'environment'"
        }
      },
      "tagName9": {
        "type": "String",
        "metadata": {
          "displayName": "Ninth Tag Name",
          "description": "Name of the tag, such as 'environment'"
        }
      }
    },
    "policyRule": {
      "if": {
        "anyOf": [
          {
            "field": "[concat('tags[', parameters('tagName1'), ']')]",
            "exists": "false"
          },
          {
            "field": "[concat('tags[', parameters('tagName2'), ']')]",
            "exists": "false"
          },
          {
            "field": "[concat('tags[', parameters('tagName3'), ']')]",
            "exists": "false"
          },
          {
            "field": "[concat('tags[', parameters('tagName4'), ']')]",
            "exists": "false"
          },
          {
            "field": "[concat('tags[', parameters('tagName5'), ']')]",
            "exists": "false"
          },
          {
            "field": "[concat('tags[', parameters('tagName6'), ']')]",
            "exists": "false"
          },
          {
            "field": "[concat('tags[', parameters('tagName7'), ']')]",
            "exists": "false"
          },
          {
            "field": "[concat('tags[', parameters('tagName8'), ']')]",
            "exists": "false"
          },
          {
            "field": "[concat('tags[', parameters('tagName9'), ']')]",
            "exists": "false"
          }
        ]
      },
      "then": {
        "effect": "modify",
        "details": {
          "roleDefinitionIds": [
            "/providers/Microsoft.Authorization/roleDefinitions/b24988ac-6180-42a0-ab88-20f7382dd24c"
          ],
          "operations": [
            {
              "operation": "add",
              "field": "[concat('tags[', parameters('tagName1'), ']')]",
              "value": "[resourceGroup().tags[parameters('tagName1')]]"
            },
            {
              "operation": "add",
              "field": "[concat('tags[', parameters('tagName2'), ']')]",
              "value": "[resourceGroup().tags[parameters('tagName2')]]"
            },
            {
              "operation": "add",
              "field": "[concat('tags[', parameters('tagName3'), ']')]",
              "value": "[resourceGroup().tags[parameters('tagName3')]]"
            },
            {
              "operation": "add",
              "field": "[concat('tags[', parameters('tagName4'), ']')]",
              "value": "[resourceGroup().tags[parameters('tagName4')]]"
            },
            {
              "operation": "add",
              "field": "[concat('tags[', parameters('tagName5'), ']')]",
              "value": "[resourceGroup().tags[parameters('tagName5')]]"
            },
            {
              "operation": "add",
              "field": "[concat('tags[', parameters('tagName6'), ']')]",
              "value": "[resourceGroup().tags[parameters('tagName6')]]"
            },
            {
              "operation": "add",
              "field": "[concat('tags[', parameters('tagName7'), ']')]",
              "value": "[resourceGroup().tags[parameters('tagName7')]]"
            },
            {
              "operation": "add",
              "field": "[concat('tags[', parameters('tagName8'), ']')]",
              "value": "[resourceGroup().tags[parameters('tagName8')]]"
            },
            {
              "operation": "add",
              "field": "[concat('tags[', parameters('tagName9'), ']')]",
              "value": "[resourceGroup().tags[parameters('tagName9')]]"
            }
          ]
        }
      }
    }
  }
}
```

Assign the policy to a subscription and list all Tags to inherit from Resource Group to resources in the "Parameters" tab.

Create a Managed Identity and a remediation task to update existing resources.

Once created the remediation task should run. Review if the policy works by checking on the remediation task once it finished and check the result.
