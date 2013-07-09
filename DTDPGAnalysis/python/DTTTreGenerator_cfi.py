import FWCore.ParameterSet.Config as cms

myDTNtuple = cms.EDAnalyzer('TTreeGenerator',
                              outputFile =cms.string("DTTree.root"),
                              dtDigiLabel = cms.InputTag("muonDTDigis"),
                              dtSegmentLabel = cms.InputTag("dt4DSegments"),
                              cscSegmentLabel = cms.InputTag("cscSegments"),
                              dtTrigDCCLabel = cms.InputTag("dttfunpacker"),
                              dtTrigSimDCCLabel = cms.InputTag("simDtTriggerPrimitiveDigis"),
                              dtTrigDDULabel = cms.InputTag("dtunpacker"),
                              staMuLabel     = cms.InputTag("muons"),
                              gmtLabel     = cms.InputTag("gtDigis"),
                              gtLabel      = cms.InputTag("gtDigis"),
                              rpcRecHitLabel = cms.InputTag("rpcRecHits"),
                              dtDigiSize = cms.int32(300),
                              dtSegmentSize = cms.int32(50),
                              cscSegmentSize = cms.int32(50),
                              dtTrigDCCSize = cms.int32(50),
                              dtTrigDCCThSize = cms.int32(50),
                              dtTrigSimDCCSize = cms.int32(50),
                              dtTrigSimDCCThSize = cms.int32(50),
                              dtTrigDDUSize = cms.int32(50),
                              gmtSize       = cms.int32(50),
                              STAMuSize     = cms.int32(20),
                              rpcRecHitSize = cms.int32(300),
                              PrimaryVertexTag = cms.InputTag("offlinePrimaryVertices"),
                              TriggerTag = cms.InputTag("TriggerResults::HLT"),
                              beamSpotTag = cms.InputTag("offlineBeamSpot"),
                              scalersResults = cms.InputTag("scalersRawToDigi"),
                              runOnRaw = cms.bool(True),
                              runOnSimulation = cms.bool(False)
)
