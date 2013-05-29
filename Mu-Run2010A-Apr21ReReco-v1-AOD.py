import FWCore.ParameterSet.Config as cms

process = cms.Process("ISPY")
process.load("ISpy/Analyzers/ISpy_AOD_Producer_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.GlobalTag.globaltag = 'FT_R_42_V10A::All'

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/FA4B49AE-366D-E011-B1B1-1CC1DE1CDF2A.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/F6F2C354-226D-E011-8D4C-1CC1DE1CDF2A.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/F01C845A-246D-E011-BB2D-1CC1DE046F78.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/E6D976D4-0E6D-E011-9DDB-1CC1DE047FD8.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/E6587EF9-216D-E011-967B-00237DA15C96.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/E4571F3E-356D-E011-8BF4-1CC1DE1CE01A.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/E2D0B346-216D-E011-B441-1CC1DE051038.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/E0C47ADC-316D-E011-B6D1-0017A4770828.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/E0B0AA51-326D-E011-9EB7-1CC1DE1D0600.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/DE08A45C-2D6D-E011-A2F4-00237DA1ED1C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/D8E35AC6-196D-E011-BF49-001A4BE1C5D4.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/D2014FCC-1B6D-E011-B2EF-1CC1DE1CEFE0.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/CED36C0B-326D-E011-B59A-1CC1DE1CDF2A.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/CECABE51-206D-E011-9AF5-00237DA13C2E.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/CE8A0D54-2D6D-E011-96D5-001E0B48A1C4.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/CA6DC37B-166D-E011-805B-0017A4770404.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/CA6C5D58-146D-E011-AC7C-00237DA1985A.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/C8BE690B-0F6D-E011-9EB5-001E0B5FC57A.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/C880165A-246D-E011-9088-78E7D164BFC8.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/C0921E55-2B6D-E011-AE62-0017A4770030.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/C05FA331-166D-E011-885D-1CC1DE0540F0.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/C04DD98A-166D-E011-8F5C-1CC1DE0540F0.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/BA15F4ED-1C6D-E011-8237-001E0BEACAB8.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/B8F2CA16-386D-E011-9DF3-78E7D1E49B52.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/B6C2A8FE-216D-E011-96F5-0017A4771028.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/B4C97B91-116D-E011-B8B8-00237DA10D14.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/B245E9B0-326D-E011-81C0-00237DA13FB6.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/B0F866BE-0F6D-E011-A0D7-0017A4770410.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/AE480B37-2C6D-E011-B0EE-00237DA1ED1C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/AABBA3EF-2F6D-E011-9A20-0017A4771028.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/A40E9F24-176D-E011-8EBB-1CC1DE047F98.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/9EFB6753-1A6D-E011-958D-0018FEFA56AE.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/9E07DAA8-2D6D-E011-BFAB-0017A4770830.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/9A492B10-376D-E011-BBCE-1CC1DE1D03DE.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/9A1D94FE-106D-E011-8883-0017A477101C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/96104900-1B6D-E011-8555-001F29C4A312.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/90A96CC5-306D-E011-B695-0017A4770C0C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/90803F85-306D-E011-87BF-0025B3E0216C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/8E630489-186D-E011-A3CB-001E0B5FD4A6.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/8AE65815-316D-E011-82D5-1CC1DE1D16AA.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/8A15131C-196D-E011-A327-1CC1DE0437C8.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/86FD8F84-186D-E011-900D-0017A4770C2C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/866A8DD0-1B6D-E011-8A08-0017A4770C0C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/84EF7D4F-296D-E011-BED8-1CC1DE1D208E.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/84600989-116D-E011-9577-00237DA1FC56.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/7CB26E48-116D-E011-AE8F-001F296A371E.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/7C8424D1-376D-E011-B8D3-0017A4771028.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/7A27521C-196D-E011-BA25-1CC1DE1CF1BA.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/7A070DD7-0E6D-E011-8930-1CC1DE1D014A.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/6E29184A-116D-E011-BE2E-00237DA12FB2.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/6E21794C-1F6D-E011-B673-001B78CE74FE.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/6C590341-2E6D-E011-99D2-0025B3E0216C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/6C307D7B-166D-E011-8739-00237DA16692.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/6ABF8FDF-126D-E011-B0C6-1CC1DE048FB0.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/6A8CD622-1B6D-E011-BDA9-00237DA13C76.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/6A7A00DD-206D-E011-9D3D-1CC1DE0500F0.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/66F599C5-136D-E011-90A2-0017A477080C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/66DF53CE-166D-E011-AE92-002481A8A782.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/668A9FCC-126D-E011-903A-1CC1DE0590E8.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/620B10DF-176D-E011-8A43-001E0B5FD4A6.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/60478C2D-136D-E011-9AFC-001E0B5FE542.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/6030E463-2D6D-E011-956E-78E7D164BFC8.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/5EE978A0-0E6D-E011-B800-00237DA1B34E.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/5EDD385A-0F6D-E011-93C2-1CC1DE1D014A.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/5CFB0AE9-326D-E011-BF94-0025B3E0216C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/5CCB1994-126D-E011-A583-0017A4771010.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/5CC8DF5A-246D-E011-BA37-001E0B479F9E.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/58EDC34C-196D-E011-9FEE-0017A4770030.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/58E16892-126D-E011-ADC1-1CC1DE048FB0.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/5846BD2A-2F6D-E011-83A2-0025B3E0216C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/56996F49-216D-E011-9553-1CC1DE1CDCAE.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/5224F78B-346D-E011-811A-0025B3E02292.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/4C025C5A-246D-E011-950C-1CC1DE046F78.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/484DDD88-376D-E011-849E-0017A4770C1C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/40CFDFAD-0E6D-E011-AF0B-00237D9F2120.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/3E63ACCC-276D-E011-B5B0-1CC1DE1CF1F6.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/3C9514FD-0E6D-E011-9D7F-1CC1DE047F98.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/3C0FC064-316D-E011-AA1E-1CC1DE1CDF2A.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/3AF5EDE7-2D6D-E011-8540-00237DA15C7C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/34E07D13-1A6D-E011-8BBB-0017A4770C2C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/34C7C88B-336D-E011-993D-0017A477080C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/342B3D63-1A6D-E011-ABA5-00237DA1985A.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/32E7793D-1C6D-E011-A7F5-00237DA15F56.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/2ADAFD66-246D-E011-AAA1-001F296BB3B8.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/2A96F959-246D-E011-B79E-00237DA1680E.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/28612BC3-1F6D-E011-92FE-0017A4770404.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/2801315A-1F6D-E011-B7B1-00237DA13C2E.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/22E9B158-366D-E011-9A55-1CC1DE0590E8.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/222B10F1-1B6D-E011-9BB9-0017A4770008.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/1CD9BAB2-2A6D-E011-9147-1CC1DE041FD8.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/161B26D8-356D-E011-93A4-1CC1DE1CE01A.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/12C41791-2C6D-E011-B0D7-001F296A371E.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/10013868-136D-E011-B81A-00237DA1985A.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/06D1433B-0F6D-E011-848E-001E0B5F27BC.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/06BF40CC-2E6D-E011-B679-001E0BEACAB8.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/0664BCC9-1A6D-E011-97AB-0017A4771828.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/04C5C95C-2F6D-E011-BE45-0017A477081C.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/02679D73-226D-E011-BC0F-1CC1DE0500F0.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/00952A46-1E6D-E011-A0C7-0017A4771038.root',
'/store/data/Run2010A/Mu/AOD/Apr21ReReco-v1/0000/004A22ED-1F6D-E011-9A6A-1CC1DE1CE026.root'))
 
from FWCore.MessageLogger.MessageLogger_cfi import *

process.add_(
    cms.Service("ISpyService",
    outputFileName = cms.untracked.string('req.ig'),
    outputMaxEvents = cms.untracked.int32(10)
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

process.p1 = cms.Path(process.iSpy_sequence)