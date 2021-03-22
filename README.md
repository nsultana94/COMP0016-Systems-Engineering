Deployment details are contained in the deployment folder of the repository.

Deployment details are also listed below.

Sharepoint Deployment
--------------------------------------------------------------------------------------------------------

Script to run for deployment:

1. $adminSiteUrl = "https://team29webapp-admin.sharepoint.com" (Admin puts in their own
Sharepoint value)

2. Connect-SPOService $adminSiteUrl (Needed for login)

3. $siteScriptFile = "C:\Users\hemil\Desktop\cfpportal.json" (Directory of the script)

4. $webTemplate = "64"

5. $siteScriptTitle = "CFP Portal"

6. $siteDesignTitle = "CFP Portal"

7. $siteDesignDescription = "Team 27 Sharepoint Deployment"

8. $siteScript = (Get-Content $siteScriptFile -Raw | Add-SPOSiteScript -Title $siteScriptTitle) | Select -First 1 Id

9. Add-SPOSiteDesign -SiteScripts $siteScript.Id -Title $siteDesignTitle -WebTemplate $webTemplate -Description $siteDesignDescription

10.  Using siteId generated by running step 9:
(This deletes the site design and this step must be run once the site is deployed)
Remove-SPOSiteDesign -Identity $siteDesignId

The site script file is contained in the google drive link below, as well as the relevant power automate flows and some videos guiding you through the set up. There are three flows exported as zips: the project proposal flow, the feedback flow and the approval flow. The videos will guide you to import these flows as well as set up the site. The site script will create the lists for you, however the styling of the site must be done by you afterwards.

https://drive.google.com/drive/folders/1qwu_olDBiciilCAbnHcX4YiU-SN6IpJV?usp=sharing

Link to duplicate form: https://forms.office.com/Pages/ShareFormPage.aspx?id=_oivH5ipW0yTySEKEdmlwuaS2kBwR75BhHpYlnK_ZSNUOTMzSEY2WVlMVTZNTk9WM0kwQzBMREU5Si4u&sharetoken=uxspDoRNmVON9e0RaLUW

-----------------------------------------------------------------------------------------------------------

