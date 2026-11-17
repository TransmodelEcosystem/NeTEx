# Changelog

## v2.0.0

This is a major release, with work going back to as far as late 2020.

### How to test your feeds & upgrade them

Data producers are encouraged to use XSD validation tooling in order to detect & upgrade their data feeds. To do so, clone the repository locally & validate against `xsd/NeTEx_publication.xsd` (the entry point).

If you think you found a bug, or have a question, [please provide feedback here](https://github.com/TransmodelEcosystem/NeTEx/issues).

### Structural changes:

* BREAKING: many version schemas now enforce stricter validation semantics: mandatory `id`/`ref`/`version` attributes were introduced or tightened in numerous object/ref structures.
* BREAKING: Several constraints were reshaped (including removal of `@order` from some keys and selective cardinality/type adjustments), which can change pass/fail outcomes for existing XML instances.
* Key/unique/keyref definitions were expanded or renamed across frames and domain modules; reference integrity checks are broader and stricter in v2.0 validation contexts.
* Publication-level schemas add or adjust integrity scopes and align naming of site/path navigation key sets.

### Functional changes (technically non-BREAKING) include:

Functional evolutions are largely additive, but existing datasets should be revalidated out of precaution.

* Addition of DECK PLAN and all related elements
* Addition of languages attributes when using MultilingualString to handle translations of names, instead of using AlternativeName
* Creation of privateCodes allowing several PrivateCode for the same element (e.g., ticketing, scheduling, etc.)
* Changes to BookingArrangement and its use for flexible services, including relation to ServiceJourneyPattern
* Addition of a relation between Facilities and Line
* Clarification of abstracts elements
* Addition and/or correction of values in enumerations (e.g., MedicalFacility, PassengerCommsFacility, SameZone, QuayType, PurchaseMoment, etc.)
* Addition of enumerations such as PropulsionTypes, FuelTypes
* Deprecation marking for several elements such as Order, PrivateCode, FlexibleLine, BaselineVersionRef, ExternalOperatorRef, PropulsionType, FuelType

---
## v1.3.1 (EPIAP)

* EPIAP to Master by @skinkie in https://github.com/TransmodelEcosystem/NeTEx/pull/705
* Add properties to describe the height of a Lift by @juliustens-db in https://github.com/TransmodelEcosystem/NeTEx/pull/696
* Fix typo by @skinkie in https://github.com/TransmodelEcosystem/NeTEx/pull/722
* Update neTactileActuators attribute on Escalators and Travelators #665tex_ifopt_equipmentAccess_version.xsd by @ue71603 in https://github.com/TransmodelEcosystem/NeTEx/pull/720
* Update netex_facility_support.xsd by @ue71603 in https://github.com/TransmodelEcosystem/NeTEx/pull/724
* TypeOfEntity is abstract by @skinkie in https://github.com/TransmodelEcosystem/NeTEx/pull/723
* Fixes from #721 by @skinkie in https://github.com/TransmodelEcosystem/NeTEx/pull/725

---
## Version 1.2.2 - Revised to add New Modes

The Part 1, Part 2, & Part 3 Schemas include   corrections and enhancements since the issue of the Version 1.2 CEN Specification documents for NeTEx.
A new Part5 is added for new modes, with examples
The new Part 5 CEN Specification document describes the additions and changes.

### 2021.09.01  NewModes: CommentAction Add __PoolOfVehicles__.
* Add  __mustpickupanddropoffInSameZone_  value to __mobilityConstraintZone__ restiction values.
* Add __PoolOfVehicles__ to Mobility Service Zonstraint zone package. Add uniqueness constraint.
* Add __PoolOfVehicles__to __MobilityServiceFrame__.
* Add __MobilityServiceConstraintZone__ to Network access right validity parameters.
* _Updates to xml schema_:
    * netex_netex_nm_mobilityConstraintZone_support.xsd
    * netex_netex_nm_mobilityConstraintZone_version.xsd
    * netex_netex_nm_mobilityServiceFrame_version.xsd
    * netex_netex_nm_mobilityJourneyFrame_version.xsd
    * netex_nm_vehicleParkingAreaInformation_version.xsd
    * netex_ifopt_parking_support.xsd
    * netex_accessRightParameter_version.xsd
    * netex_publication_version.xsd
* _Updates to xml examples_:
    * NewModes-CycleSharingExample.xml

### 2021.08.30  NewModes: CommentAction: Add policy url attributes
* Add to __SharingPolicyUrl__ attribute to __VehicleSharingService__ and  __PoolingPolicyUrl__ attribute to __VehiclePoolingService___.
* _Updates to xml schema_:
    * netex_netex_nm_mobilityService_version.xsd

### 2021.05.03  NewModes: GBFS compatibility AT#1 __MobilityConstraintZone__ add __ZoneRuleApplicability__ add _inside_  and _outside_.

* Add _enclosed_ value to  __ParkingLayout__ enumeration
* _Updates to xml schema_:
    * netex_mobilityZerviceConstraintZone_support.xsd.xsd
### 2021.04.18  NewModes: GBFS compatibility AT#1 __DataSource__ add __DataLicenceCode__ and __DataLicenceUrl__  to __DataSource__.
* Add _enclosed_ value to  __ParkingLayout__ enumeration
* _Updates to xml schema_:
    * netex_mobilityZerviceConstraintZone_support.xsd.xsd
    * netex_mobilityZerviceConstraintZone_version.xsd.xsd
* _Updates to xml examples_:
    * NewModes-CycleSharingExample.xml

### 2021.04.15  NewModes: GBFS compatibility AT#1 Add _car_ as enum value to to __Vehicle__  / _vehicle Types_.
__ParkingProperties__
* Add __BayGeometry__, __ParkingVisibility__ with values.
* Add _enclosed_ value to  __ParkingLayout__ enumeration.
* _Updates to xml schema_:
    * netex_vehicle_type_support.xsd.xsd
    * netex_parking_support.xsd.xsd
    * netex_parking_version.xsd.xsd
* _Updates to xml examples_:
    * NewModes-CycleSharingExample.xml
    * NewModes-CarPoolingExample.xml.

### 2021.04.15  NewModes: Revise AT#8 Add __ShortName__ to __MobilityService__.
* _Updates to xml schema_:
    * netex_mobility_service.xsd.xsd

### 2021.04.15  NewModes: Revise AT#8 Facilities: AT#8 add  _scooterHire_ to value to __HireFacility__ enumeration.
* Align __Hirefacility__ values with spec and add  new __Mode__ values _scooterHire_, _vehicleHire_, _boatHire_ and _other_.
* Add _docks_ to __CycleStorage__ enumeration.
* _Updates to xml schema_:
    * netex_ifopt_localServiceCommercial_support.xsd.xsd
    * netex_ifopt_mobilityService_version.xsd.
    * netex_ifopt_equipmentParking_support.xsd
    * netex_facility_support.xsd.xsd
* _Updates to xml examples_:
    * NewModes-CycleSharingExample.xml
    * NewModes-CarPoolingExample.xsd

### 2021.04.14  NewModes: Revise AT#8 add  _mobileAppInstallCheck_ to value to __infoLinkTypes__ enumeration.
* _Updates to xml schema_:
    * netex_utility_types.xsd
* _Updates to xml examples_:
    * NewModes-CycleSharingExample.xml

### 2021.04.14  NewModes: Revise AT#9 Add missing enum values to __MobilityConstraintZone__. __TransportZoneUseEnumeration__:  _allUsesAllowed_ and _noPassThrough_ .
* _Updates to xml schema_:
    * netex_nm_mobilityServiceConstraintZone_version.xsd
* _Updates to xml examples_:
    * NewModes-CycleSharingExample.xml

### 2021.03.10  NewModes: Revisions to support GBS. add _targetPlatform_ attribute to  _InfoLink_.
* New modes: add  target platform to attributes of  __InfoLink__.
* _Updates to xml schema_:
    * netex_utilityTypes.xsd

### 2021.03.10  NewModes: Revisions to support GBFS.
* Add _RentalAvailability_ and _ParkingBayCondition_.
* _Updates to xml schema_:
    * RENAME parkingBayStatus to netex_nm_vehicleParkingAreaInformation_support.xsd
    * RENAME nm_mobilityJourneyFrame_version.xsd
    * netex_nm_publication_version.xsd
    * netex_all_objects_part5_newModes.xsd
    * netex_nm_mobilityJourneyFrame_version.xsd
    * NeTEx.SPP
    * NeTEx.xpr
* _Updates to xml examples_:
    * NewModes-CarPoolingExample.xsd

### 2021.01.29  Bug Issue #143 Correct data type of __GapToPlatform__.
* _Updates to xml schema_:
    * netex_equipmentVehiclePassenger_version.xsd.xsd

### 2021.01.10  NewModes: Revisions.
* Add constraint for __ModeRestrictionAssessment__.
* Add unverified status to  __AccountStatusType__.
* __Customer__: Add EMail and Phone  verification flag.
* Add __allVehicles__ enbum value to   __SelfDriveMode__ values.
* _Updates to xml examples_:
    * NewModes-CarPoolingExample.xsd
    * NewModes-CyclePoolingExample.xsd
    * NewModes-CyclePoolingExample.xsd
* _Updates to xml schema_:
    * netex_mobilityService_version.xsd
    * netex_salesContract_support.xsd
    * netex_salesContract_version.xsd
    * netex_nm_publication_version.xsd

### 2021.01.08  NewModes: Revisions.
* Rename __PersonalVehicleType__ to __SimpleVehicleType__.
* Drop __MobilityServiceElement__ and use __DistanceMatricElement__ instead.
* _Updates to xml examples_:
    * NewModes-CarPoolingExample.xsd
    * NewModes-CyclePoolingExample.xsd
    * NewModes-CyclePoolingExample.xsd
* _Updates to xml schema_:
    * netex_distanceMatrixElement_version.xsd
    * netex_farsStructureElement_version.xsd
    * netex_nm_publication_version.xsd
    * REMOVE netex_nm_mobilityServiceElement_support.xsd
    * REMOVE netex_nm_mobilityServiceElement_version.xsd
### 2020.12.11  NewModes: Revisions
* Rename __PersonalVehicleType__ to __SimpleVehicleType__.
* Drop __PublicTransportOrganisationType__.
* Add expiry date to __AccessCode__.
* _Updates to xml schema_:
    * netex_submmode_version.xsd
    * netex_mode_version.xsd
    * netex_mode_support.xsd
    * netex_vehicleType_support.xsd
    * netex_vehicleType_version.xsd
    * netex_transportOrganisation_support.xsd
    * netex_transportOrganisation_version.xsd
    * netex_mobilityService_support.xsd
    * netex_mobilityService_version.xsd
    * netex_onlineService_version.xsd
    * netex_trainElement_version.xsd
    * netex_accessCredentials_version.xsd

### 2020.11.06  NewModes: Corrections
* Drop unused __ContinuousModes__ enumeration.
* _Updates to xml schema_:
    * netex_mode_support.xsd

### 2020.11.06  NewModes: Corrections
* Correct __ParkingEquipment__ supertypes.
* _Updates to xml schema_:
    * netex_nm_parkingEquipment_version.xsd
    * netex_nm_parkingEquipmentsupport.xsd
    * netex_nm_parkingEquipment_version.xsd

### 2020.11.12  NewModes: Corrections
* Rename __ModelEquipmentProfile__ to __VehicleModelProfile__,  __CycleEquipmentProfile__ to __CycleModelProfile__, ,  __CarEquipmentProfile__ to __CarModelProfile__
* Correct comments and missing types.  Move __Contact__ into organisation package.
* _Updates to xml examples_:
    * NEW NewModes-CarPoolingExample.xsd
    * NEW NewModes-CyclePoolingExample.xsd
* _Updates to xml schema_:
    * netex_nm_vehicleType_support.xsd
    * netex_nm_fleetEquipment_support.xsd
    * netex_nm_fleetEquipment_version.xsd
    * netex_publication.xsd

### 2020.11.06  NewModes: Corrections
* Rename __GeneralVehiclePooling__ to __CarPoolingService__.
* Correct comments and missing types.  Move __Contact__ into organisation package.
* _Updates to xml examples_:
    * NEW NewModes-CarPoolingExample.xsd
* _Updates to xml schema_:
    * netex_organisation_support.xsd
    * netex_organisation_version.xsd
    * netex_transportOrganisation_version.xsd
    * netex_nm_mobilityService_support.xsd
    * netex_nm_mobilityService_version.xsd
    * netex_publication.xsd

### 2020.11.06  NewModes (Norway):  Enhace Organisations
* Add relationship between organisations:  * Add __RelatedOrganisation__, with __OrganisationRole__ enumerations.
* Add reusable __Contact__ details.
* _Updates to xml schema_:
    * netex_organisation_support.xsd
    * netex_organisation_version.xsd
    * netex_transportOrganisation_version.xsd
    * netex_all_objects_generic.xsd
    * netex_salesDistribution_version.xsd
    * netex_publication.xsd
    * NeTEx,SPP

### 2020.11.06  Incorporate master udpates :
* Issue #124,   Add _multimodalQuay_ enumeration  to __Quay__.
* Fix typo on __AllInclusivePriceType__.
* _Updates to xml schema_:
    * netex_all_frames_framework.xsd
    * netex_stopPlace_support.xsd
    * netex_facilityUic_support.xsd

### 2020.10.21  NewModes : Car service example and miscellaneous small revisions.
* Add XML Example of  Chauffeured car service; revise schema to enable.
    * NewModes: Add __MobilityServiceElement__ to __Tariff__.
* Geofencing:
    * Add new __MobilityServiceConstraintZone__ : for geofenceing. Add to __ResourceFrame__.
    * __RoutingConstraintZone__ : Add _forbiddenZone_, _passThroughUseOnly_, _cannotBoardInZone_ and _mustAlightInZone_ to  __ZoneUse__.
* Individual Traveller:
    * Add __IndividualTraveller__  with __IndividualTravellerInfo__ and __VehiclePoolingDriverInfo__,
    * Add _member_ and _other_ to __UserProfile__ __UserType__ enumeration.
    * Add _unspecified_ enum value to   __GenderEnumeration__, for use in __IndividualTraveller__.
* Usage Paremeters:
    * Rename __HireChargePolicy__ to __RentalChargePolicy__ and move to separate rental operations package.
    * Add _fine_ and _findHandlingFee_ to __RentalPolicy__ values.
* Vehicles:
    * Add __PropulsionType__ (with enum values) and __MaximumRange__ to __TransportType__,
    * Add __Description__, and __ModelProfileRef__  to __Vehicle__,
    * Rename __TypeofFuel__ to __FuelType__ (Depreceate __TypeOfFuel__),
* __Parking__ add open vehicle types using __TransportTypeRef__.
* _Updates to xml examples_:
    * NEW NewModes-ChauffeuredServiceExample.xsd
* _Updates to xml schema_:
    * netex_routingConstraint_support.xsd
    * NEW netex_mobilityServiceConstraint_support.xsd
    * NEW netex_mobilityServiceConstraint_version.xsd
    * netex_distribution_support.xsd
    * netex_parking_support.xsd
    * netex_parking_version.xsd
    * netex_equipmentENergySupport_support.xsd
    * netex_fareStructureElement_support.xsd
    * NEW netex_nm_individualTraveller_support.xsd
    * NEW netex_nm_individualTraveller_version.xsd
    * netex_vehicleType_support.xsd
    * netex_vehicleType_version.xsd
    * netex_all_objects_part5_newModes.xsd

### 2020.10.20  NewModes : Car pooling example and miscellaneous small revisions.
* NewModes:Add XML Example of Car Pooling Service, revise  schema to enable.
* Frames
    * TM Support: __SalesTransactionFrame__ : Add __MediumAccessDevice__.
    * General: __ResourceFrame__ :  Add __FacilitySets__.
*  __ConditionSummary__ (for __FareProduct__ and __SalesOfferPackage__):  Add __RentalConditionSummaryGroup__.
* Utility types: __InfoLinks__ add _mobileAppDownload_ value to __infoLinkTypes__ enumeration.
* Facilities:  Add _AnimalsAllowed_   enum value  to __NuisanceFacility__. Add missing _taxiRank_  enumeration value to __StopPlaceType__,
* _Updates to xml schema_:
    * NEW NewModes-CarPoolingExample.xsd
    * netex_salesContract_version.xsd
    * netex_salesTransaction_version.xsd
    * netex_usageParameterEligibility_support.xsd
    * netex_facility_support.xsd
    * netex_parkingSupport_version.xsd
    * netex_utilityTypes_version.xsd
    * netex_resourceFrame_version.xsd
    * netex_customerEligibility_version.xsd

### 2020.10.16  NewModes : Cycle example and miscellaneous small revisions.
* NewModes: Add XML Example of Cycle Sharing service, revise to enable new features.
* Usage Parameters
    * New Modes: __UsageValidityPeriod__ : __ Add _accessCode_ value to __ActivationMeans__ enumeration.
    * NewModes: Add new __HirePenaltyPolicy__ parameter with _noVehicleReturn_, _lateVehicleReturn_, _damageToVehicle_, _damageToEquipment_, etc, values.
    * NewModes: __ChargingPolicy__ : Add __DepositPolicy__ attribute  with enum values.
* Fare Product
    * NewModes: Add __RequiresDeposit__ and __NoCashPayment__ to __CommercialConditionSummary__.
    * FIX:  __ChargingMomementType__ add new value _beforeTravelThenAdjustAtEndOfTravel_; correct typo on _beforeStartThenAdjustAtEndOfFareDay__
* Fare Table:
    * Add __EquipmentRef__ to __FareTable__ and __Cell__ specifics.
* Organisation:
    * NewModes: __Organisation__; Add __onlineProvider__ to __OrganisationType__ enumeration
* Equipment:
    * NewModes: Add _docks_ value  to __CycleStorageType__ enumeration values.
    * __LuggageStorageFacilities__: add enumeration values _skiRacks_ and _skiRacksAtRear_.
* Network Restriction
    * NewModes: __NetworkRestrictions__ : Widen all  references __VehicleTypeRef__ to be __TransportTypeRef__
* _Updates to xml schema_:
    * NEW NewModes-CycleSharingExample.xsd
    * netex_organisation_support.xsd
    * netex_equipmentParking_support.xsd
    * netex_facility_support.xsd
    * netex_networkRestriction_version.xsd
    * netex_parking_version.xsd
    * netex_usageParameterTravel_support.xsd
    * netex_usageParameterCharging_support.xsd
    * netex_usageParameterCharging_version.xsd
    * netex_fareTable_version.xsd
    * netex_usageParameterCharging_version.xsd
    * netex_nm_accessCredentialAssignment_version.xsd
    * netex_conditionSummary_support.xsd

### 2020.10.15  NewModes : Revise condition summary.
*  NewModes: __FareProduct__ / __ConditionSummary__: Add __Mode__ and __ModeOfOperation__.
*  FIX: __Site__: Add _transport_ value  to __SiteType__ enumeration values.
* _Updates to xml schema_:
    * netex_site_support.xsd
    * netex_resourceFrame_version.xsd
    * netex_conditionSummary_support.xsd

### 2020.10.15  NewModes : Add Constraints for NewMode entities.
* _Updates to xml schema_:
    * netex_networkRestriction_version.xsd
    * netex_nm_publication_version.xsd

### 2020.10.15  NewModes : Revise Frames
* _Updates to xml schema_:
    * netex_nm_mobilityServiceFrame_version.xsd
    * netex_nm_vehicleMeetingPoint_version.xsd
    * netex_nm_singleJourneyPath_version.xsd

### 2020.10.15  NewModes : Add attributes from IXSO
* NewModes:Update __FleetEquipment__: add attributes from IXSO.
* _Updates to xml schema_:
    * netex_nm_fleetEquipment_support.xsd
    * netex_nm_fleetEquipment_version.xsd

### 2020.10.15  NewModes : Fares  support.
* NewModes: Add __LocalServiceRef__ and __MobilityServiceRef__  to __Tariff__ applicability.
* NewModes: Add  __MobilityServiceElement__  and __MobilityServiceElementPrice__.
* _Updates to xml schema_:
    * netex_fareStructureElement_version.xsd
    * netex_ifopt_allObjects.xsd
    * NEW netex_nm_mobilityServiceElement_support.xsd
    * NEW netex_nm_mobilityServiceElement_version.xsd

### 2020.10.14  NewModes :  Parking Caspacity.
* NewModes: Add __ParkingCapacityAssignment__
* _Updates to xml schema_:
    * netex_ifopt_allObjects.xsd
    * NEW netex_nm_parkingCapacityAssignment_support.xsd
    * NEW netex_nm_parkingCapacityAssignment_version.xsd

### 2020.10.14  NewModes : Corrections to "all object" include files,
* FIX: Clean up all_object includes. Add missing files.
* _Updates to xml schema_:
    * netex.spp
    * netex_ifopt_allObjects.xsd
    * DELETE netex_accounting_version.xsd
    * netex_allObjects_part2_journeyTimes.xsd
    * netex_allObjects_reusableComponents.xsd
    * netex_all_objects_part3_salesTransactions

### 2020.10.14  NewModes : Revise __Parking__ model.
* NewModes: Add __VehicleServiceParkingBay__ and __ParkingBayStatus__ .
* _Updates to xml schema_:
    * netex_all_objects_part5_newModes.xsd
    * netex_nm_parkingBayStatus_support.xsd
    * netex_nm_parkingBayVersion_version.xsd.

### 2020.10.13  NewModes : Fare model updates.
* NewModes: __CustomerPurchasePackage__: Add __MediumApplicationRef__.
* NewModes: Eligibility  __UsageParameter__:  Add __VehiclePoolerProfile__.
* _Updates to xml schema_:
    * netex_netex_customerPurchasePackage_version.xsd
    * netex_nm_usageParameterEligibility_support.xsd
    * netex_nm_usageParameterEligibility_version.xsd.
    * netex_nm_salesContract_version.xsd.

### 2020.10.11  NewModes:  File reorganise and rename to follow dependencies
* TIDY UP Move prerequisite  files to NeTEx framework. Add "nm" to file name to distinguish.
* _Updates to xml schema_:
    * MOVE to RC: netex_netex_nm_fleet_support.xsd
    * MOVE to RC: netex_netex_nm_fleet_version.xsd
    * MOVE to RC: netex_netex_nm_fleetEquipment_support.xsd
    * MOVE to RC: netex_netex_nm_fleetEquipment_version.xsd
    * MOVE to IFOPT: netex_taxiPlace_support.xsd
    * MOVE to IFOPT: netex_taxiPlace_version.xsd
    * MOVE to FM_ST:  netex_mediumAplication_support.xsd
    * MOVE to FM_ST:  netex_mediumApplication_version.xsd
    * MOVE to FM_ST:  netex_customerPaymentMeans_support.xsd
    * MOVE to FM_ST:  netex_customerPaymentMeans_version.xsd
    * RENAME as netex_netex_nm_fleet_version.xsd
    * RENAME as  netex_netex_nm_fleet_support.xsd
    * RENAME as  netex_netex_nm_fleet_version.xsd
    * RENAME as  netex_netex_nm_fleetEquipment_support.xsd
    * RENAME as  netex_netex_nm_fleetEquipment_version.xsd
    * RENAME as  netex_netex_nm_mobilityService_support.xsd
    * RENAME as  netex_netex_nm_mobilityService_version.xsd
    * RENAME as  netex_netex_nm_onlineService_support.xsd
    * RENAME as  netex_netex_nm_onlineService_version.xsd
    * RENAME as  netex_nm_vehicleMeetingPoint_support.xsd
    * RENAME as  netex_nm_vehicleMeetingPoint_version.xsd
    * RENAME as  netex_nm_vehicleMeetingPointAssignment_support.xsd
    * RENAME as  netex_nm_vehicleMeetingPointAssignment_version.xsd
    * RENAME as  netex_nm_taxiPlace_support.xsd
    * RENAME as  netex_nm_taxiPlace_vesion.xsd
    * RENAME as  netex_nm_vehicleMeetingPlace_support.xsd
    * RENAME as  netex_nm_vehicleMeetingPlace_vesion.xsd
    * RENAME as  netex_nm_vehicleAccessCredentials_support.xsd
    * RENAME as  netex_nm_vehicleAccessCredentials_vesion.xsd

### 2020.10.11 NewModes  Price Tidy ups - update references, fixes.
* NewModes __FareTable___ Update __CellReferences__:
    * Add __VehicleTypeRef__ .  __VehicleModelRef__,  __ModelEquipmentRef__, __EquipmentRef__.
* _Updates to xml schema_:
    * netex_fareTable_version.xsd

### 2020.10.09  NewModes  Tidy ups - update references, fixes.
*  NewModes: revise __TravelSpecificationSummary__:
* Add __VehicleMeetingPoint__ and __VehicleMeetingPlace__ to __TravelSpecificationSummaryEndpoint__.
* __TravelSpecificationSummary__: Add __SingleJourneyRef__.
* NewModes: Widen  refernce to use __TransportOrganisationRef__ rather than __OperatorRef__
    * Revise reference:  __TravelSpecificationSummaryEndpoint__.
    * Revise reference:  __SiteConnection__.
    * Revise reference:  __FareTable__.
    * Revise reference:  __JourneyDesignator__.
* NewModes: Widen  reference to use __TransportTypeRef_ rather than __VehicleRef__.
    * Revise reference:  __TimetableFrame__.
    * Revise reference:  __ParkingTariff__,  __Parking_Properties__.
    * Revise reference:  __Fleet__.
* Revise reference:  __SingleJourneyPath__: Add __OnwardMeetingLinkRef__ to __PointInSingleJourneyPath__.
* __FareTable__ : Add __SingleJourneyRef__, __GroupOfSingleJourneysRef__.
* _Updates to xml schema_:
    * netex_travelSpecificationSummary_version.xsd
    * netex_timetableFrame_version.xsd
    * netex_siteConnection_version.xsd
    * netex_fleet_version.xsd
    * netex_singleJourneyPath_version.xsd
    * netex_journeyDesignator_support.xsd
    * netex_parkingTariff_version.xsd
    * netex_fareTable_version.xsd

### 2020.10.09  NewModes:  Revise booking arrangements
* NewModes: Add  __ServiceBookingArrangement__ to  __MobilityService__.
* General: Add further __PaymentMethodType__ enum values; _mobileApp_ and _atCounter_ to __BookingMethod__ .
* _Updates to xml schema_:
    * netex_serviceRestriction_support.xsd
    * netex_serviceRestriction_version.xsd
    * netex_usageParameterBooking_support.xsd
    * netex_usageParameterBooking_version.xsd

### 2020.10.09  NewModes:  Allow a colour to be associated with a parking etc.
* NewModes: Add  __Presentation__ to  __SiteElement__.
* _Updates to xml schema_:
    * netex_ifopt_site_version.xsd

### 2020.10.07  NewModes  Add new frames
* NewModes: Add  __MobilityServiceFrame__ and __MobilityJourneyFrame__.
* Updates to xml schema_:
    * netex_all_objects_part5_newModes.xsd
* NEW netex_mobilityServiceFrame_version.xsd
    * NEW netex_mobilityJourneyFrame_version.xsd

### 2020.10.07  NewModes:  Make new mode elements assignable as fare parameters.
* Add  parameters to  __ValidityParameterAssignments__.
* _Updates to xml schema_:
    * netex_all_objects_part5_newModes.xsd

### 2020.10.07  NewModes:  Implement TM6.0 Fare entities not yet in NeTEx.
* Add  __MediumAccessDevice__, __CustomerPaymentMeans__.
* _Updates to xml schema_:
    * netex_all_objects_part5_newModes.xsd
    * NEW netex_mediumApplication_support.xsd
    * NEW netex_mediumApplication_version.xsd
    * NEW netex_customerMeans_support.xsd
    * NEW netex_customerMeans_version.xsd
    * NEW netex_vehicleAccessCredentials_support.xsd
    * NEW netex_vehicleAccessCredentials_version.xsd
    * netex_salesContract_support.xsd

### 2020.10.07  NewModes: Equipment additions.
* NewModes: Add  __VehicleReleaseEquipment__,  __RefuellingEquipment__ ,
* NewModes: __TransportType__: Add __ModelProfile__.
* _Updates to xml schema_:
    * netex_all_objects_part5_newModes.xsd
    * netex_parkingEquipment_support.xsd
    * netex_parkingEquipment_version.xsd
    * netex_vehicleType_support.xsd
    * netex_vehicleType_version.xsd
    * NEW netex_fleetEquipment_support.xsd
    * NEW netex_fleetEquipment_version.xsd
    * NEW netex_equipmentEnergy_support.xsd
    * NEW netex_equipmentEnergy_version.xsd

### 2020.10.06  NewModes:  Add single journey support.
* NewModes: Add    __SingleJourney__ and    ___SingleJourneyPath__.
* NewModes: Add __ModeRestrictionAsssessment__ to __RouteLink__.
* _Updates to xml schema_:
    * netex_all_objects_part5_newModes.xsd
    * NEW netex_singleJourney_support.xsd
    * NEW netex_singleJourney_version.xsd
    * NEW netex_singleJourneyPath_support.xsd
    * NEW netex_singleJourneyPath_version.xsd
    * NEW netex_vehicleServicePlaceAssignment_support.xsd
    * NEW netex_vehicleServicePlaceAssignment_version.xsd
    * netex_route_support.xsd
    * netex_route_version.xsd

### 2020.10.06 NewModes:  Add topology elements;  points, places and assignments.
* NewModes: Add  __VehicleMeetingPooint__ and    ___VehicleMeetingLink__.
* NewModes: Add  __VehicleMeetingPlace__ and    ___VehicleServicePlaceAssignments__, with subtypes.
* NewModes: Add __VehicleMeetingPoint__ to __Connection__ end.
* _Updates to xml schema_:
    * netex_all_objects_part5_newModes.xsd
    * NEW netex_vehicleMeetingPoint_support.xsd
    * NEW netex_vehicleMeetingPoint_vesion.xsd
    * NEW netex_vehicleMeetingPointAssignment_support.xsd
    * NEW netex_vehicleMeetingPointAssignment_version.xsd
    * NEW netex_taxiPlace_support.xsd
    * NEW netex_taxiPlace_vesion.xsd
    * NEW netex_vehicleMeetingPlace_support.xsd
    * NEW netex_vehicleMeetingPlace_vesion.xsd
    * netex_servicePattern_version.xsd

### 2020.10.04  NewModes: Update responsibility role types.
* NewModes: Add new enumeration values for  __StakeholderRoleType__ and    __DataRoleType__.
* _Updates to xml schema_:
    * netex_responsibilities_support.xsd

### 2020.10.04  NewModes: Add mobility services.
* NewModes: Add  __MobilityService__ and subtypes, add __OnlineServiceOperator__.
* _Updates to xml schema_:
    * netex_all_objects_part5_newModes.xsd
    * NEW netex_mobilityService_support.xsd
    * NEW netex_mobilityService_version.xsd
    * NEW netex_onlineService_support.xsd
    * NEW netex_onlineService_version.xsd
    * netex.spp

### 2020.10.04  NewModes:  Revise  __VehicleType__
* Add __TransportType__ and __PersonalTransportType__.
* _Updates to xml schema_:
    * NEW netex_fleet_support.xsd
    * NEW netex_fleet_version.xsd
    * netex_vehicleType_support.xsd
    * netex_vehicleType_version.xsd
    * netex_train_support.xsd
    * netex_train_version.xsd
    * netex_vehicleJourney_version.xsd
    * netex_all_objects_reusableComponents.xsd
    * NEW netex_all_objects_newModes.xsd

### 2020.10.04  NewModes  Revise Transport Organisations.
* NewModes: Add  __TransportOrganisation__ and __PublicTransportOrganisation__.
* _Updates to xml schema_:
    * netex_transportOrganisation_support.xsd
    * netex_transportOrganisation_version.xsd

### 2020.10.04  NewModes:  Add  references to __ModeOfOperation__.
* NewModes: Update existing references to __Mode__ to include __ModeOfOperation__.
* _Updates to xml schema_:
    * netex_transportOrganisation_version.xsd
    * netex_vehicleType_version.xsd
    * netex_stopPlace_version.xsd
    * netex_flexiblStopPlace_version.xsd
    * netex_equipmentTicketing_version.xsd
    * netex_equipmentSigns_version.xsd
    * netex_access_version.xsd
    * netex_line_version.xsd
    * netex_servicePattern_version.xsd
    * netex_assistenceBooking_version.xsd
    * netex_accessRightParameter_version.xsd
    * netex_usageParameterTravel_version.xsd
    * netex_fareFrame_version.xsd

### 2020.10.04  NewModes : Revise modes
* NewModes Add __ModeOfOperation__.
* FIX: Also correct typos in __Notice__  file.
* _Updates to xml schema_:
    * NEW netex_modeOfOperation_support.xsd
    * NEW netex_modeOfOperation_version.xsd
    * netex_mode_support.xsd
    * netex_mode_version.xsd
    * netex_notice_version.xsd
    * netex.spp

----
## Version 1.1.2 - Base version plus further minor fixes comprising.

### 2020.08.11  Update Oxygen project to include new examples
* _Other updates_:
    * netex.xpr
* _Updates to examples_:
    * \examples\standards\era_uic\Netex_Eurostar mapping_era_1.xml
    * \examples\standards\era_uic\Netex_Eurostar mapping_era_2.xml
    * \examples\standards\era_uic\Netex_era_uic_joiningsplitting.xml
    * \examples\standards\era_uic\Netex_era_uic_timetable_hack_01.xml
    * \examples\standards\norway\stops\BasicStopPlace_example.xml

### 2020.08.11   FIX  Issue #110 Add missing fuel types to  __VehicleType__  /  __FuelType__
* Additional values:  _electricContact, battery, dieselBatteryHybrid, petrolBatteryHybrid, biodiesel, hydrogen, liquidGas, methane, ethanol_.
* _Updates to xml schema_:
    * netex_framework\netex_reusableComponents\netex_vehicleType_support.xsd

### 2020.08.11  FIX  Issue #106 *Schema*: Add missing constraints for allow __GeneralZone__ and __AdministrativeZone__
* _Updates to xml schema_:
    * netex_publication_version.xsd

### 2020.08.11   FIX  Issue #104 *Framework*: Add __ResponsibilityRole__    in __ResourceFrame__
* _Updates to xml schema_:
    * netex_framework\netex_frames\netex_resourceFrame_version.xsd"

### 2020.08.10  FIX  Issue #108 *Framework*: Allow __ServiceCalendar__ to hold __UuicOperatingPeriod__
* _Updates to xml schema_:
    * netex_framework\netex_reusableComponents\netex_serviceCalendar_support.xsd
    * netex_framework\netex_reusableComponents\netex_serviceCalendar_version.xsd
    * netex_publication_version.xsd
* _Updates to examples_:
    * Add NTA XML examples

### 2020.07.29 FIX  Issue #97 *Part2*: Add __NormalDatedJourney__ and __DatedVehicleJourney__ to journeys  in __TimetableFrame__.
* _Updates to xml schema_:
    * netex_part2\netex_journeyTimes\netex_datedVehicleJourney_version.xsd

----
## Version 1.1.1 - Updated NeTEx Schema
The Part 1, Part 2, & Part 3 Schemas include minor corrections and enhancements since the issue of the Version 1.0 documents.
The revised Version 1.1 documents include the changes.
Base version plus further minor fixes comprising##

### 2020.07.28 EXAMPLES  Revise fare examples.
* _Updates to xml schema_:
* NONE
* _Updates to xml examples_:
    * Extensive

### 2020.07.28 FIX Issue #101*Publication*:Add missing constraints for __FareTableRow__, __FareTableColumn__, __TypeOfLine__ and for __FareZone__ Parent,
* _Updates to xml schema_:
* netex_framework/netex_genericFramework/netex_publication_version.xsd
* _Updates to xml examples_:
* Netex_era_distance_ro.xml.

### 2020.07.28   FIX  Issue #100*FRAMEWORK*: Correct the substitution group on OrganisationUnit.
* _Updates to xml schema_:
* netex_framework/netex_genericFramework/netex_organisation_version.xsd

### 2020.06.21 FIX Issue #75*FRAMEWORK*: __FareClass__ Remove space from end of __secondClass__ enumeration value.
* _Updates to xml schema_:
* netex_framework/netex_reusableComponents/netex_serviceRestrictions_support.xsd

### 2020.06.21 PARTIAL FIX Issue #73*PART2*:Recursive includes:
* NJSK  Remove cyclic inclusion dependency.
* _Updates to xml schema_:
* netex_flexibleService Journey.xml

### 2020.06.21 FIX  Issue #78 *PART2*:Journey Coupling:
* NJSK  __JourneyCouple__ / __MainPartRef__ should be of type  __JourneyPartRef__.
* _Updates to xml schema_:
* netex_coupledJourney.xml

### 2020.06.21 FIX  Issue #92 *FRAMEWORK*:LinkProjection NJSK
* Expose the missing __EntityInVersion__ elements on the __LinkProjection__ derivation
* _Updates to xml schema_:
* netex_projectionVersion.xml

----
## Version 1.1.0 - Base version plus minor fixes comprising
* Norway contributions,
* The approved 1.1 CRs 1-50
* Rollup of fixes and additional documentation on other fixes.
* Corrections to integration of NK  1.09.
* 51-55 CRs from Meeting Feb 2019. Also CRs from NL, EURA, UK,  Norway and SBB input.

The Part 1, Part 2, & Part 3 Schemas include minor  corrections and enhancements since the issue of the Version 1.0 documents.
The revised Version 1.1 documents include the changes.

### 2019.05.17 FIX  *PART3:FARES*: NJSK  __FarePointInPattern__  Fix case on __isFareStage__ and __isForbidden__
* _Updates to xml schema_:
    * netex_production.xml

### 2019.05.15 FIX  *PART1:ND*: NJSK  Add constraints  on __TypeOfLineRef__
* _Updates to xml schema_:
    * netex_publication.xml

### 2019.05.14 EXMP  *FRAMEWORK*: NJSK  Add Serbia and Montenegro to country codes
* _Updates to xml schema_:
    * netex_countrySupport.xml

### 2019.05.10 EXMP  *EXAMPLES*: NJSK  Revise UK examples to have UK Profile data.
* _Updates to xml examples_:  Many

### 2019.05.19 FIX  *PART1:ND*: NJSK  Fix - remove empty value for CompassBearing enum
* _Updates to xml schema_:
    * netex_locationTypes.xml
    * netex_routeInstructionVersion.xml

### 2019.05.02 FIX  *FRAMEWORK*: NJSK  Fix constraints  on __DefaultCodespaceRef__
* Also Corrections to a lot of examples.
* _Updates to xml schema_:
    * netex_publication.xml

### 2019.05.01 FIX  *FRAMEWORK*: NJSK  Fix constraints  on __DefaultDataSourceRef__ and __DefaultResponsibilitySetRef__.
* ALso add EPIP draft profile metadata
* _Updates to xml schema_:
    * netex_publication.xml
    * netex.spp
* _Updates to xml examples_:
    * uk_fxc_addon_HSP_plusbus.xml
    * Netex_era_toc_uk.xml
    * Netex_era_crossborder_de.xml
    * uk_fxc_pass_Metrobus_metrorider.xml
    * uk_fxc_trip_First_WoE_Line48_stage+Passes.xml
    * uk_fxc_trip_First_WoE_Line48_stage-distance_minimal1.xml
    * Netex_tap_tsi_tcvg_stations_1.xml
    * epip_common_profile.xml

### 2019.04.29 FIX  *PART2:ND*: NJSK  Fix Constraints  on __JourneyPart__.
* _Updates to xml schema_:
    * netex_publication.xml

### 2019.04.28 FIX  *FRAMEWORK*: NJSK  Fix Constraints  on __ParkingPassengerEntrance__ and __VehicleEntranceForParking__.
* _Updates to xml schema_:
    * netex_publication.xml
    * netex_parking_support.xml
    * netex_parking_version.xml

### 2019.05.01 FIX  *Parts2VS*: NJSK  Fix Add missing _ParentRef__ to __FlexibleService__.
* Also add missing flexble attributes to __SpecialService__
* _Updates to xml schema_:
    * netex_flexibleService.xml
    * netex_ServiceJourney.xml

### 2019.04.29 FIX  *PART1:ND*: NJSK  Fix Dummy __TariffZone__ should be abstract.
* _Updates to xml schema_:
    * netex_zone_version.xml

### 2019.04.29 FIX  *PART2:ND*: NJSK  Fix Constraints  on __JourneyPart__.
* _Updates to xml schema_:
* netex_publication.xml

### 2019.04.19 __CHECKPOINT__.
- Revised  v1.1 versions of NeTEx UML diagrams, and revised draft NeTEx Part1, Part2 and Part3 documents correspond to this point.

### 2019.04.19 FIX  *Parts3FARES3*: NJSK  Add missing __TypeOfFareTable__ element.
* _Updates to xml schema_:
    * netex_fareTable_version.xml

### 2019.04.18 FIX  *Parts3FARES3*: NJSK  Support Place to Place travel.
*  __AccessRightParameter__: Add __AddressRef__,  __TopoographicPlaceRef__ and __PlaceUseEnum__.
*  __InterchangeRule__   use of __ServiceDesignator__ versus __JourneyDesignator__
* _Updates to xml schema_:
    * netex_accessRightParameter_support.xml
    * netex_accessRightParameter_version.xml
    * netex_travelSpecificationSummary_version.xml

### 2019.04.18 FIX  *Parts1,2,3*: NJSK  Fix: Tidy up Designators.
* __AccessRightParameter__: Add __AddressRef__,  __TopoographicPlaceRef__ and __PlaceUseEnum__.
* Modularise __ServiceDesignator__ and __JourneyDesignator__ (no functional change).
* Add __JourneyDesignator__ to __InterchangeRule__ and __GroupOfServiceJourneysMember__.
* _Updates to xml schema_:
    * netex_journeyDesignator_support.xml
    * netex_interchangeRuletravelSpecificationSummary_version.xml
    * netex_serviceJourney_version.xml

### 2019.04.16 FIXDoc *Part1-IFOPT*: NJSK __Parking__ - correct dependencies.
* Drop __Parking / tariffs relationship__: __ParkingTariff__ can reference __Parking__ but not vice  versa.
* Also add missing parents to __ParkingCapacity__.
* NB this will break existing XML that uses __Parking / charges__ relationship.
* _Updates to xml schema_:
    * netex_par	*king_version.xml
* _Updates to xml examples_:
    * netex_10_StopPlace_withParking_1.xml
    * netex_21_Sites_Parking_1.xml
    * netex_21_Sites_Parking_2.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.04.16 FIXDoc *Part1-IFOPT*: NJSKCorrect __VehicleStoppingPosition__ to reflect UML model.
* Add missing elements to implement relationships between components.
* _Updates to xml schema_:
    * netex_stopPlace_version .xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.04.15 FIXDoc *Part1-TP*: NJSK __TimeDemandType__: Add missing __OperationalContextRef__.
* _Updates to xml schema_:
    * netex_timedDemandType_version .xml
    * netex_stopPlace_version .xml
* _Documentation Changes_:  [uml_diagram: ok], [doc-done]

### 2019.04.15 FIXDoc *Part1-IFOPT*: NJSK Fix __TypeOfEntity__ and __TypeofValue__ descendants to make root elements visible.
* _Updates to xml schema_:
    * netex_organisation_version.xsd
    * netex_responsibilitySet_version.xsd
    * netex_place_version.xsd
    * netex_pointAndLink_version.xsd
    * netex_pointAndLinkSequence_version.xsd
    * netex_projection_version.xsd
    * netex_spatialFeature_version.xsd
    * netex_zone_version.xsd
    * netex_equipment_version.xsd
    * netex_facility_version.xsd
    * netex_notice_version.xsd
    * netex_securityList_version.xsd
    * netex_serviceRestrictions_version.xsd
    * netex_activation_version.xsd
    * netex_line_version.xsd
    * netex_journeyPattern_version.xsd
    * netex_timeDemandType_version.xsd
    * netex_ifopt_checkConstraint_version.xsd
    * netex_ifopt_serviceFeature_version.xsd
    * netex_flexibleService_version.xsd
    * netex_accessRightParameter_version.xsd
    * netex_fareStructureElement_version.xsd
    * netex_salesOfferPackage_version.xsd
    * netex_retailConsortium_version.xsd
    * netex_salesContract_version.xsd
    * netex_coupledJourney_version.xsd
    * netex_usageParameter_version.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-done]

### 2019.04.15 __FIXDoc__ *Part1-IFOPT*: NJSK Fix Add missing __CountryRef__ to __Authority__.
* Align __Authority__ with __Operator__.
* _Updates to xml schema_:
    * netex_transportOperator_version.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.04.15 __FIXDoc__ *Part1-IFOPT*: NJSK Fix add missing __typesOfEntity/TypeOfEntity__  relationship to __TypeOfFrame__.
* _Updates to xml schema_:
*  netex_responsibility.xml
* netex_typeOfFrame_version.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.04.15 __FIXDoc__ *Part1-IFOPT*: NJSK Fix add missing element from doc  to __TypeOfPassengerInformationEquipment__.
* _Updates to xml schema_:
    * netex_passengerInformationEquipment_version.xml
* _Documentation Changes_:  [uml_diagram: ok], [doc-ok]

### 2019.04.14 __FIXDoc__ *Part1-RC*: NJSK Fix __Accommodation__ and __OnBoardStay__ - add missing parent elements.
* Correct typo on __BoardingPermission__.
* NB THis will break existing documents that use ths feature
* _Updates to xml schema_:
    * netex_serviceRestrictions_version.xml.
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.04.07 __FIXDoc__ *Part1-IFOPT*: NJSK Add back missing attribute to __SanitaryEquipment  / NumberofToilets__.
* Align schema With UML and document.
* _Updates to xml schema_:
    * netex_passengerEquipment_version .xml
* _Documentation Changes_:  [uml_diagram: ok], [doc-ok]

### 2019.04.07 __FIX__   *Part3FARES-ST*: NJSK Tidy up - remodularise: move __TravelSpecification__ to be with __CustomerPurchasePackage__.
* Also revise __FareProduct__ classification types.
* _Updates to xml schema_:
    * netex_fareStructureElement_support.xsd
    * netex_fareProduct_support.xsd
    * netex_fareProduct_version.xsd
    * netex_fareConditionSummary_support.xsd
    * netex_travelDocument_version.xsd
    * netex_salesTransaction_support.xsd
    * netex_salesTransaction_version.xsd
    * netex_customerPurchasePackage_support.xsd
    * netex_customerPurchasePackage_version.xsd
    * netex_travelSpecifcationSummary_version.xsd
* _Updates to xml examples_:
    * uk_fxc_pass_Metrobus_metrorider.xml
    * netex_era_distance_ro.xml
    * netex_era_crossborder_de.xml
    * netex_era_toc_uk.xml
    * uk_fxc_trip_First_York_Line26_stage-Z2Z_minimal1.xml
    * uk_fxc_trip_First_WoE_Line48_stage-distance_minima1.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.04.04  __FIXDoc__  *PART2-VJ*: NJSK Fix  Add missing __ConnectionCertainty__ element that is in doc.
* Add new __ConnectionCertainty__ attribute to __Interchange__ as per UML diagrams and doc.
* _Updates to xml schema_:
    * netex_interchange_support.xsd
    * netex_interchange_version.xsd
* _Documentation Changes_:  [uml_diagram: ok], [doc-ok]

### 2019.04.04  __FIXDoc__  *Part3-FARES-AR*: NJSK Further tidy ups arising from doc.
* Add new value to __PreassignedFareProduct / Product__ enumeration;  _shortTrip_.
* Add new value to __AmountOfPriceUnit / ProductType__ numeration; _storedValue_.
* Add new  attribute __ProductType__ to  __UsageDiscountRight__ with values _mileagePoints, usageRebate, other_.
* Add new  attribute  __ProductType__ to __SaleDiscountRight__ with values;  _travelCard, payAsYouGoDiscount, other_.
* Add new values to __SupplementProductType__; _penalty_.
* Add new __ChargingMomentType__ attribute to __FareProduct__ with values: _beforeTravel, onStartOfTravel, beforeEndOfTravel, onStartThenAdjustAtEndOfTravel, onStarThenAdjustAtEndOfFareDay, onStartThenAdjustAtEndOfChargePeriod, atEndOfTravel, atEndOfFareDay, atEndOfChargePeriod, free, other_.
* Also remodularise: move __TariffBasisEnum__ to _netex.fareElement_support.xsd_.
* Add new __TypeOfSalesOfferPackage__ attribute to __ValidityParameterAssignment__. Reorganise fare parameters.
* _Updates to xml schema_:
    * netex_fareStructureElement_support.xsd
    * netex_fareProduct_support.xsd
    * netex_fareProduct_version.xsd
    * netex_fareConditionSummary_support.xsd
    * netex_validityParameterAssignment_version.xsd
    * netex_facility_version.xsd
* _Updates to xml examples_:
    * uk_fxc_pass_Metrobus_metrorider.xml
    * netex_era_distance_ro.xml
    * netex_era_crossborder_de.xml
    * netex_era_toc_uk.xml
    * uk_fxc_trip_First_York_Line26_stage-Z2Z_minimal1.xml
    * uk_fxc_trip_First_WoE_Line48_stage-distance_minimal1.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.04.02 __FIX__ *PART2*: Add TransportOperatorRef to JourneyDesignator
* _Updates to xml schema_:
    * netex_journeyDesignator_support.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.30  __EURA-52, EURA40__ *Part3-FARES-AR*:  Support suspension of season passes.
* NJSK Review: Make __Suspending__ a  separate usage parameter,  with attributes __SuspensionPolicy, QualificationPeriod, QualificationPercent,  MinimumSuspensionPeriod, MaximumSuspensionPeriod, MaximumNumberOfSuspensionsPerTerm__.
* _Updates to xml schema_:
    * netex_usageParameterTravel_support.xsd.
    * netex_usageParameterTravel_version.xsd.
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.30 __FR49__ *Part1-IFOPT*:  CD #65 Accessibility changes,
* Fix add missing __DropKerbOutside__ attribute  to __EntranceEquipment__.
* NJSK Review: Rename __LuggageService__ new attribute  __LuggageMaxiumWeight__ new attribute to  to __MaximumBagWeight__.
* NJSK Review: Rename  __Entrance__ new attribute __OpeningNecssaryForce__ to __NecessaryForceToOpen__.
* NJSK Review: Move  __Stair__ new attribute __WithoutRiser__ to __StairCase__ (does not apply to escalators).
* NJSK Review: Rename __PathLink__ new attribute __Width__ to __MinimumWidth__ also add __MinimumHeight__.
* NJSK Review: Add value _alwaysOn_ to __LightingMethodEnumeration__. Rename to __LightingOnMethod__.
* NJSK Review: Systemise; for __SignEquipment__  : reuse  __AudioTriggerMethod__ rather than have separate valeu set
* NJSK review: Add __PrintedPresentation__ to __SignEquipment__ rather than simple __FontSize__ so as to separate presentation from content.
* NJSK review: Add __FontSizeEnum__ to __PrintedPresentation__ as a general property.
* NJSK Review: Revise __PassengerSafetyEquipment__ , rename  'Acoustic' to 'Audio'. rename app _value_ to _mobileApp_, add _cyclicReadingValue_
* _Updates to xml schema_:
    * netex_ifopt_equipmentTicketing_version.xsd
    * netex_ifopt_localService_version.xsd
    * netex_ifopt_equipmentAccess_support.xsd
    * netex_ifopt_equipmentAccess_ version.xsd
    * netex_ifopt_path_support.xsd
    * netex_ifopt_path_ version.xsd
    * netex_ifopt_equipmentPassenger_support.xsd
    * netex_ifopt_equipmentWaiting_support.xsd
    * netex_ifopt_equipmentWaiting_version.xsd
    * netex_ifopt_equipmentSign_support.xsd
    * netex_ifopt_equipmentSign_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.26 __UK-27__ *FRAMEWORK-RC*: NJSK Fix add missing __TrainSize__ attribute to __TrainElement__.
* Align doc with schema.
* _Updates to xml schema_:
    * netex_line_support.xsd
    * netex_trsinElement_version.xsd
    * netex_vehicleJourney_version.xsd
* _Documentation Changes_:  [uml_diagram: ok], [doc-done]

### 2019.03.26 __UK-27__ *Fares-ST*: NJSK Correct annotations, reorder parameters,
* Add __TypeOfProductCategoryRef__ to __TravelSpecificationSummary__, fix __CellRef__ .
* Make __TravelDOcumentRef__ many-to-one.as per TM.
* Also EURA-(nk)Allow marking of use of __CustomerPurchasePackage__. Refine model: make blocking separate from status. Correct annotations.
* Wrap __CustomerPurchasePackage /TravelDocRef__   in  a tag.
* Align doc with schema.
* Reorganize fare examples.
* _Updates to xml schema_:
    * netex_salesTransaction_version.xsd
    * netex_travelDocument_version.xsd
    * netex_salesDistribution_support.xsd
    * netex_travelSpecificationSummary_version.xsd
    * netex_customerPurchasePackage_support.xsd
    * netex_customerPurchasePackage_version.xsd
* _Updates to xml examples_:
  * uk_fxc_pass_Metrobus_metrorider.xml
  * netex_era_distance_ro.xml
  * netex_era_crossborder_de.xml
  * netex_era_toc_uk.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.26 __NL27__ *Part1-ND*: CD #58  Add default  __TypeOfProductCategory__ and __TypeOfService__ to __Line__:
* CD  Move __TypeOfProductCategory__ and __TypeOfService__ to _netex_line_version.xsd_.
* NJSK Review:  Move __TypeOfProductCategory__ and __TypeOfService__  from (Part2:) _netex_journey_version.xsd_   to (Framework reusable component)  _netex_travelRights_version.xsd_)- rather than _line.xsd_,  so they are visible to part 1.
* NJSK Review: clean up dependencies.
    * Drop include of _netex_travelRights_version.xsd_ from _netex_accessRightParameter_version.xsd_.
    * Drop include of _netex_travelRights_version.xsd_ from _netex_usageParameterAfterSales_version.xsd_.
    * Drop include of _netex_travelRights_version.xsd_ from _netex_fareTable_version.xsd_.
    * Drop include of _netex_travelRights_version.xsd_ from _netex_parking_version.xsd_.
* NJSK Review: Rename _netex_travelRights_version.xsd_ to _netex_servicRetrictions.xsd_ so as to align with TM6 and UML.
* NJSK Review: correct the annotations.  Also align _Netex.xpr_ with _Netex.spp_ and correct _Netex.spp_ project files for _XMLSpy_ and _Oxygen_.
* _Updates to xml schema_:
    * netex_serviceJourney_support.xsd
    * netex_servicePattern_support.xsd
    * netex_serviceRestrictions_support.xsd (renamed from netex_travelRights_support.xsd)
    * netex_serviceRestrictions_version.xsd (renamed from netex_travelRights_version.xsd)
    * netex_line_version.xsd
    * netex_accessRightParameter_version.xsd
    * netex_usageParameterAfterSales_version.xsd.
    * netex_fareTable_version.xsd
    * netex_parking_version.xsd
    * netex.spp
    * netex.xpr
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __FR49__ *Part1-IFOPT*:  CD #65 Accessibility changes.
* __TicketingEquipment__ (_netex_ifopt_equipmentTicketing_.xsd):
    * CD Add new attributes to __TicketingEquipment__; __TactileInterfaceAvailable, AudioInterfaceAvailable, DisabledPriority, WheelchairSuitable__.
    * NJSK Review: Place  accessibility attributes in a separate group. Break down into subgroups;  __TicketingEquipmentPropertiesGroup, TicketingEquipmentServiceGroup, TicketingEquipmentAccessibilityGroup__.
    * CD: Add  new attributes to __TicketValidatorEquipment__; __AudioValidationFeedback, VisualValidationFeedback, TactileValidationFeedback, ValidationGuidance__.
* __LocalService__ ( _netex_ifopt_localService.xsd_):
    * CD add __LuggageMaximalWeihgt__ to __LuggageService__.
    * NJSK Review: Correct Typo and revise name on __LuggageMaximumWeight__ to MaximumBagWeight.  Make datatype of __LuggageMaximumWeight__  _WeightType_. Also add to __LeftLuggageService__.
* __AccessEquipment__ (_netex_ifopt_equipmentAccess_.xsd):
    * CD Add __NecessaryForce__ to __Entrance__ with values _noForce, lightForce, mediumForce,  heavyForce, unknown_.
    * CD Add __LightingMethodEnumeration__ to __PlaceLighting__ with values _movementDetector, stepDetector, switchOnTheWall,
      atDoorOpening, onlyAtNight_.
    * NJSK Review: Correct typo on _stepDetector_.
    * CD Add __TactileWarningStripEnumeration__ to __CrossingEquipment__ with values _tactileStripAtBeginning, tactileStripAtEnd, 	tactileStripAtBothEnds, noTactileStrip, unknown_,
    * NJSK Review:  Move __TactileWarningStripEnumeration, FlooringTypeEnumeration, BorderTypeEnumeration__ to _netex_ifopt_equipmentAccess,xsd_ from _netex_path_support.sd_; use lower camel case for values.
    * CD Add new attribute __NecessaryForceEnumeration__ with values _noForce, lightForce, mediumForce,  heavyForce, unknown_.
    * CD Add new attribute __LightingMethod__ to __PlaceLighting__ with values _movementDetector, stepDetector, switchOnTheWall, atDoorOpening, onlyAtNight, other_.
    * NJSK Review:  correct typo on _stepDetector_.
    * CD Add new attribute __WithoutRiser__ to __StairEquipment__.
    * NJSK Review: Change order of new elements to be with other  step properties.
    * CD  Add new attribute __EscalatorWithLanding__ to __EscalatorEquipment__.
    * CD  Add new attributes to __TravelatorEquipment__; __Length__, __Slope__ and __IntegratesAnEscalatorPart__.
    * NJSK Review:  correct  name of __IntegratesAnEscalatorPart__
    * CD Add new attributes  to __EscalatorEquipment__: __MagneticInductionLoop__, __GroundMarkAlignedWithButton__, __TactileGroundFloorButton__,  __ExternalFloorSelection__.
    * NJSK Review: Correct  name of __GroundMarkAlignedWithButton__.
    * NJSK Review: Drop __ButtonsHeigt__ as all ready covered  by __CallButtonHeight__.
    * NJSK Review: Change order to group with like properties.
    * CD Add new attributes  to __EntranceEquipment__: __AudioOrVideoIntercom, Airlock, DoorstepMark AudioPassthroughIndicator, OpeningNecessaryForce__
    * NJSK Review: Change order of new elements to group with like properties
    * NJSK Review: NB __AudioOrVideoIntercom__ overlaps with __EntranceAttention__.
    * CD Add new attributes  to __QueuingEquipment__:  __DisabledPriority, QueuingSeatedPossible.__
* __PathLink__ (_netex_ifopt_path.xsd_):
    * CD Add new attributes to __PathLink__;  __Width, FlooringType,  RightSideBorder,  LeftSideBordert, TiltAngle, CodedTilt, TactileWarningStrip,  TactileGuidingStrip__.
    * NJSK Review: Reorder so as to place like elements together, add XML sub groups to organize
    * _netex_ifopt_equipmentPassenger_:
        * CD Add __FlooringTypeEnumeration__ to __PathLink__ with values _carpet, concrete, asphalt, cork, fibreglassGrating, glazedCeramicTiles, plasticMatting, ceramicTiles, rubber, steelPlate, vinyl, wood, stone, grass, dirt, gravel, uneven, unknown, other_
        * CD Add __BorderTypeEnumeration__ with __PathLink__ values _wall, grass, dirt, barrier, road, cyclingLane, step, rail, plants, trees, mud, solidEdge, water, gravel, noPhysicalBorder, otherPhysicalBorder, unknown, other,_
* __PassengerEquipment__ (_netex_passengerEquipment.xsd_):
    * CD Add new attribute to __PassengerSafetyEquipment__;  __AcousticAnnouncementsTrigger__  with values _onDemand,   automatic_.
    * CD Add new attribute to __PassengerSafetyEquipment__; __AnnouncementsTriggeringMethod__  with values _presenceDetector,  app, internetPage, specificDevice, pushButton_.
    * CD add new attribute to __SanitaryEquipment__;  __SupportBarHeight__  with values _onDemand,   automatic_.
    * NJSK Review: Correct typo on __SupportBarHeigth__, reorder new elements.
    * NJSK Review: Add missing __ChangeAvailable__ attribute
* __WaitingEquipment__ (_netex_ifopt_equipmentWaiting_):
    * CD to Add new attribute to __LuggageLockerEquipment__:  __LockingType__  with values _key, keyboard, mechanicalNumbering, contactless, phoneApp, other_.
    * CD to Add new attributes to __LuggageLockerEquipment__:  __BlindAccessible ,WheelchairAccepted__.
    * NJSK Review: Correct typo on __WheelchairAccepted__, Change order of new attributes, move __LockerTypeEnumeration__  and __LuggageServiceEnumeration__ enums   to support file.
    * CD to Add new attributes to __SeatingEquipment__:  __Armrest ,SeatingHeight__.,
    * NJSK Review: Correct data type on  __SeatingHeight__. and rename to __SeatHeight__.
* __SignEquipment__ (_netex_signEquipment.xsd_):
    * CD add new attribute to __SignEquipment__; __AudioAnnouncementType__  with values _cyclicReading, whenSomebodyIsDetected, throughAnApp, throughASpecificDevice, other_
    * CD add new attribute to __SignEquipment__;  __FontSize__; with values; _verySmall, small, medium, large, veryLarge_
    * NJSK Review:  Correct typos, camelCase values, move __SignContentEnumeration__   enums   to support file , add _other_ value, zap _xxxx_value. change"big" to "large" in value names.
    * NJSK Review:  Add missing __AsBraille__ attribute from doc.
* _Updates to xml schema_:
    * netex_ifopt_equipmentTicketing_version.xsd
    * netex_ifopt_localService_version.xsd
    * netex_ifopt_equipmentAccess_support.xsd
    * netex_ifopt_equipmentAccess_ version.xsd
    * netex_ifopt_path_support.xsd
    * netex_ifopt_path_ version.xsd
    * netex_ifopt_equipmentPassenger_support.xsd
    * netex_ifopt_equipmentWaiting_support.xsd
    * netex_ifopt_equipmentWaiting_version.xsd
    * netex_ifopt_equipmentSign_support.xsd
    * netex_ifopt_equipmentSign_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __NL48__ *Part1-ND*: CD #64  Add new attributes to __StopPointInPattern__ for   advertising of stop; __Print__ and __Dynamic__.
* NJSK Review: Correct dependencies: Move  __DynamicAdvertisement__ of use of stop  from _netex_serviceJourney_support.xsd_ to _netex_servicePattern_support.xsd_.
* NJSK Review: correct the annotations.
* _Updates to xml schema_:
    * netex_serviceJourney_support.xsd
    * netex_servicePattern_support.xsd
    * netex_servicePattern_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __NL32__ *FRAMEWORK-RC*: CD #61 Add new values to SITE __AccessFacility__ enum; _wheelchairLift, automaticRamp. slidingStep_.
* NJSK Review: Keep SITE and SERVICE aspects separate; add separate __VehicleAccessFacility__ enum with values   _unknown, wheelchairLift, manualRamp, automaticRamp, steps, slidingStep, narrowEntrance, validator_.
* _Updates to xml schema_:
    * netex_facility_support.xsd
    * netex_facility_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __NL31__ *FRAMEWORK-RC*: CD #60 Add new attributes __BoardingHeight__ and __GapToPlatform__ to __VehicleType__.
* NJSK Review: Correct data types of new attributes to be of _LengthType_.
* _Updates to xml schema_:
    * netex_vehicleType_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __NL28__ *FRAMEWORK-CC*: CD #59 Add new __Presentation__ attribute to __Branding__.
* NJSK Review; Use a __BrandingGroup__ to be consistent with NeTEx coding patterns.
* _Updates to xml schema_:
    * netex_dataSource_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __SBB23__ *FRAMEWORK-CC*: CD #57. Add new __BackgroundColour__ and __BackgroundColourName__ attributes to __Presentation__ and __PrintPresentation__  elements.
* Also add _icon_ to __TypeOfInfolink__ enum values.
* NJSK Review; __BackgroundColourName__  should be  type _xsd:normalizedString_, not _xsd:string_.
* _Updates to xml schema_:
    * netex_utility_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __SBB21__ *FRAMEWORK-CC*: CD #56. Add new __ColourSystem__ attribute to __Presentation__ and __PrintPresentation__.
* NJSK Review: __ColourSystem__ and __ColourName__  should be  type _xsd:normalizedString_, not _xsd:string_.
* Also Merge in corrections to comments as per SBB20 #55.
* Also Correct camel case on names of __StopPointInXXXGroup__ groups.
* _Updates to xml schema_:
    * netex_utility_version.xsd
    * netex_servicePattern_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __FR-5__ *FRAMEWORK-CC*: CD change #53 Add __AccessFacilityList__ attribute to __SiteFacilitySet__.
* _Updates to xml schema_:
    * netex_facility_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __CR55__ *PART1-IFOPT*: CD Change #52 Add new attribute  __StopPlaceWeight__  to __StopPlace__ with values _international, national, regional, local_.
* NJSK Review: Make  values lowerCamelCase consistent with NeTEx conventions.
* _Updates to xml schema_:
    * netex_ifopt_stopPlace_support.xsd
    * netex_ifopt_stopPlace_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __CR51__ *PART2-TI*: CD Add new __VehicleJourneyStopAssignment__ entity to set default stop assignment for __VehicleJourney__.
* NJSK Review CR51:  add doc comments
* NJSK make __vehicleJourneyStopAssignmentsInFrame_RelStructure__ lower camel case consistent with NeTEx conventions.
* NJSK Allow inlining of __vehicleJourneyStopAssignments__ within __VehicleJourney__ as for other subcomponents
* NJSK Also correct camel case on __trainComponentLabelAssignents__ and __trainComponentLabelAssignents_RelStructure__.
* _Updates to xml schema_:
    * netex_vehicleJourney_support.xsd
    * netex_vehicleJourney_version.xsd
    * netex_timetableFrame_version.xsd
    * netex_stopAssignment_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __Fix__ *FRAMEWORK-FR*: Integrate constraint fix  #49 by CD 2019.02.22 with other constraint changes: Add __EquipmentPlace__  to  __Place_AnyVersionedKey__.
* _Updates to xml schema_:
    * netex_publication.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __CR50__ by CD from 2019-02-20 *FRAMEWORK-CC*.  CD add snow and ice modes.
* NJSK  Revise -
* Correct camel casing of _snowAndIce_   value for __TransportMode__,
* Correct camel casing of  __SnowAndIceSubmode__ values ; 	 _unknown, undefined,  snowMobile,  snowCat,  snowCoach,  terraBus, windSled_,
* Add _snowAndIce_ to __Submode__ choices
* Add _snowAndIce_ to __AllModes__.
* Add _ski_ and _skate_ to __AccessMode__  __ContinuousMode__ values
* _Updates to xml schema_:
    * netex_submode_version.xsd
    * netex_mode_support.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __NL34__  from 2019.01.07 *FRAMEWORK-CC*. Fix #42 by Seime & #63 by CD move  _canalBarge_ value from air to water modes.
* NB this will break existing XML that uses _canalBarge_ value.
* Also changed __Duty.TransportMode__ from __VehicleModeEnumeration__   to __AllVehicleModesOfTransportEnumeration__ to allow for non-vehicle modes.
* _Updates to xml schema_:
    * netex_submode_version.xsd
    * netex_duty_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.25 __Fix__  *FRAMEWORK-CC*:   #43 by Skinkie from 2019.01.07.
* Fix typo on _tactilePlatformEdges_.
* NB this will break existing XML that uses _tactilePlatformEdges_ value.
* _Updates to xml schema_:
    * netex_facility_support.xsd
* _Updates to xml examples_:
    * examples\functions\stopPlace\Netex_10_StopPlace_uk_ComplexStation_Wimbledon_1.xml
    * examples\functions\stopPlace\Netex_10_StopPlace_withParking_1.xml
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.03.25 __Fix__  *FRAMEWORK-CC*: #41 by Skinkie from 2019.01.07: Fix typo on __MobilityList__.  Internal change only.
* _Updates to xml schema_:
    * netex_acsb_passengerMobility.xsd
    * netex_equipmentVehiclePassenger_version.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.03.25 __Fix__ *FARES-FS*: #40 by Skinkie from 2019.01.07  Fix typo on __DistanceMatrixElement.IsDirect__.
* NB this will break existing XML that uses __IsDirect__ attribute.
* _Updates to xml schema_:
    * netex_distanceMatrixElement_version.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.03.25 __Fix__  *Part1-IFOPT*: #39 by Skinkie from 2019.01.07.
* Fix typo on __ServiceSiteRef.Structure__.
* _Updates to xml schema_:
    * netex_ifopt_site_support.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.03.25 __Fix__  *Part1-IFOPT*: Fix #38 by Skinkie from 2019.01.07
* Fix typo on __KeyScheme__.
* NB this will break existing XML that uses __KeyScheme__ attribute.
* _Updates to xml schema_:
    * netex_ifopt_equipmentPassenger_version.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.03.25 __Fix__  *PART2-DM*: Fix  #35 by Skinkie  from 209.01.03 __AccountingTime__.
* Fix typo on __AccountingTime__.
* NB This will break existing XML that uses __AccountingTime__ attribute.
* NJSK  Also add separate EndDayOffSer - DayOffSet should apply to start time relative to operatig day of Duty
* _Updates to xml schema_:
    * netex_duty_version.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.03.25 __Fix__  *PART1-ND*: #37 by Skinkie from 2019.01.07 Correct type on  __OppositeDirectionRef__.
* Correct Typo:  rename __OppositeDIrectionRef__ to __OppositeDirectionRef__.
*  NB This will break existing XML  that uses __OppositeDirectionRef__ attribute.
* _Updates to xml schema_:
    * netex_route_version.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.03.15  Small tidy ups to new value names and to documentation

### 2019.03.13 __UK-27 & FIXES__  *Part3-FARES*: Fix __FareContract__ and __CustomerPurchasePackage__ issues.
* Allow marking of use of __CustomerPurchasePackage__.
* Also  Fix several issues and align with TM6.
* UK-28  Add reference to __CustomerAccount__ to __FareContract__.
* Add new attribute __AccountStatusType__ to __CustomerAccount__.
* Add new __email__ attribute to __Customer__.
* Fix:  Add  missing relationship __fareContracts / FareContract__ to __CustomerAccount__.
* Remove __fareContractEntries__ relationship from __CustomerAccount__  : Use relationship on __FareContract__. NB BREAKAGE!
* Fix:  Add  missing relationship __customerPurchasePackageRefs /  CustomerPurchasePackage__ to __CustomerAccount__.
* Add missing attributes __CustomerRef__, __CustomerAccountRef__ and FareCOntractRef__ to __CustomerPurchasePackage__.
* Add __PassengerSeatRef__ and __TrainElementRef__ to __TravelDocument__.
* Add __PrivateCode__ to __TravelDocument__.
* Add missing __CustomerPurchasePackageRef__ to __TravelDocument__.
* Add new attribute __PassengerSeatRef__ and __TrainElementRef__ to __TravelDocument__.
* Add new attribute  __AccessNumber__ to __SpecificParameter Assignment__.
* Add new attribute  __CustomerPurchasePackageStatus__  to to __CustomerPurchasePackage__ with values _resrved_,_ordered_, _paidFor_, _unused_, _activated_ _partiallyUsed_, _used_, _archived_.
* Add new attribute __MarkedAs__ to __CustomerPurchasePackageElement__.
* Add missing relationship   __travelDocuments \ TravelDocument__   to __CustomerPurchasePackage__.
* Add new view element  __TravelSpecificationSummaryView__ to __TravelSpecification__.
* Add new view element  __TravelSpecificationSummaryView__ to __CustomerPurchasePackage__.
* Add new __CustomerPurchasePackageElementAccess__ element to __CustomerPurchasePackageElement__.
* Also UK-32 *Part3-FARES*: Add __StartDate__ and __EndDate__ attributes to __ResidentialEligibility__.
* HOUSEKEEPING Separate out  _netex_typeOfravelDocumentPackage.xsd_ from _netex_travelDocumentPackag.xsd_
* HOUSEKEEPING Move   _netex_travelDocumentPackage.xsd_ from _\fares_ to to \ _sales_Transaction_ folder.
* _Updates to xml schema_:
    * netex_typeOfTravelDocumentPackage_support.xsd (new)
    * netex_typeOfTravelDocumentPackage_version.xsd (new)
    * netex_travelSpecifcationSummaryView_version.xsd (new)
    * netex_travelDocumentPackage_support.xsd
    * netex_travelDocumenPackage_version.xsd
    * netex_customerPurchasePackage_support.xsd
    * netex_customerPurchasePackage_version.xsd
    * netex_usageParameterEligibility_support.xsd
    * netex_usageParameterEligibility_version.xsd
    * netex_salesContract_support.xsd
    * netex_salesTransaction_version.xsd
    * netex_publication.xsd
    * netex.spp
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.13 UK-27 & FIXES  *Part3-FARES*: Extend __CustomerPurchasePackage__ implementation.
* Also add  attribute __SupplementProductType__ to   __SupplementProduct__ with values    _seatReservation, bicycle, dog, animal, meal, wifi_
* _Updates to xml schema_:
    * netex_fareProduct_support.xsd
    * netex_fareProducte_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.13 EURA-29  *Part3-FARES*:    Add  new __EligibilityChangePolicy__  usage parameter.
* Wwith attributes __OnBecomingPolicy__ and __OnCeasingPolicy__.
* __OnBecomingEnumeration__.
    * _automatic_ - If user becomes eligible, automatically apply additional user profile benefits to user, e.g. apply student or senior discounts.
    * _invite_ - If user becomes eligible, invite user to take up eligible products. e.g. Invite to buy Senior railcard.
    * _noAction_ - If user becomes eligible,, no automatic measures are taken.
    * _other_
* __OnCeasingEnumeration__ - Allowed values
    * _immediateTermination_ - If user ceases to be eligible, automatically terminate validity of an  elibility dependent product.
    * _useUntilExpiry_ - If user ceases to be eligible, they may go on using the product until it  expires.
    * _terminateAfterGracePeriod_ - If user ceases to be eligible,  termination  take place after the end of a grace period.
    * _automaticallySubstituteProduct_ - If user ceases to be eligible, assign them an appropiate  replacement product.
    * _noAction_ - If user ceases to be eligible, take no action.
    * _other_
* Add integrity constraint for __EligibilityChangePolicy__.
* _Updates to xml schema_:
    * netex_usageParameterEligibility_support.xsd
    * netex_usageParameterEligibility_version.xsd
    * netex_publication.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.13 EURA-50  *Part3-FARES*: Add new __PurchaseAction__ attribute to  __PurchaseWindow__.
* With values: _purchase_,  _reserve_,  _orderWithoutPaying_,  payForPreviousOrder, other_, _seatMap_  and _openSeating_.
* Also rename  __Reserving__  \ __ReservationType__ to __SeatAllocationMethod__ and move __SeatAllocationMethodEnumeration__ to new __VehicleSeating__ package.
* Also add __ReservationExpiryPeriod__ to __Reserving__.
* _Updates to xml schema_:
    * netex_vehicleSeating_support.xsd
    * netex_usageParameterBooking_support.xsd
    * netex_usageParameterBooking_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

## 2019.03.13  EURA-40 *Part3-FARES*: Tidy up - Include new elements as fare validity parameters
* Add  new __FareStructureValidityParametersGroup__ to validity paarmaters with new attributes   __TypeOfTariffRef__,   __TypeOfFareStructureFactor__,  __TypeOfFarFresStructureFactorRef__,
* Extend  __FareProduct ValidityParametersGroup__  to validity paramaters  with new attributes   __TypeOfPriceingRuleRef__,   __ChargingMethodRef__, __TypeOfPaymentMethodRef__, __TypeOfMachineReadability__, __TypeOfFareTableRef.__
* Add  new __SeatingValidityParametersGroup__ with new attributes   __TrainElementRef__,    __TrainComponentLabelAssignmentRef__.
* Also UK-69 Scaleability. Allow classification ofto  __FareTable__ with     new __TypeOfOfFareTable__ element.
* Also Rename draft  __ValidityParameterSetOperator__ __ValidityParameterSelectionType__.
* Also UK-41  Also add new __LimitationSelectionType__ as additional functional operator to __GenericParameterAssignment__  to clarify use of groups :  _oneOf /  someOf/  allOf_.
* Also add integrity constraints for __TypeOfMachineReadability__.
* _Updates to xml schema_:
    * netex_fareTable_support.xsd
    * netex_fareTable_version.xsd
    * netex_validityCondition_support.xsd
    * netex_accessRightParameter_version.xsd
    * netex_publication.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.13  EURA-40 *Part3-FARES*:  Support Suscriptions  - additional changes.
* Also add  new attrributes to __FareProduct \ ConditionSummary__:  __PenaltyIfWithoutTicket__ and __AvailableOnSubscription__.
    * netex_conditionSummary_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done

### 2019.03.13 EURA-93, EURA-085  *Part3-FARES*: Add new attribute to  __InterChanging__, __RegisterBreak__.
* With values _none,   markByStaff,  markByValidator,  markByMobileApp, other_
* Also EURA-085  Add  new attribute __ActivationMeans__ attribute  to __UsageValidityPerido__ with values  _noneRequired, checkIn,  useOfValidato useOfMobileDevice, automaticByTime,  automaticByProximity, other_
* _Updates to xml schema_:
    * netex_usageParameterTravel_support.xsd
    * netex_usageParameterTravel_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]


### 2019.03.13 UK  *Part3-FARES*: Simplify use of Fares:
* Add new  Atrribute  __PreeassignedFareProductType__ to      __PreassignedFareProduct__ with values _singleTip,  timeTimitedSingleTrip, dayReturnTrip, periodReturnTrip, multiStepTrip, dayPass,  periodPass, other_.
* Add new attribute   __AmountOfPriceUnitType__ to     __AmountOfPriceUnitFareProduct__ with values  _tripCarnet, passCarnet, unitCoupons, other_.
* NB these are separate from __TariffBasis__.
* _Updates to xml schema_:
    * netex_fareProduct_support.xsd
    * netex_fareProduct_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.13 NORWAY-100 *Part3-FARES*: Support VAT (and other tax)  categories.
* Add __TypeOfPricingRule__  element.
* Also FIX  add missing (!) relationship  __ruleStepResults \ RuleStep__ on  __SalesTransaction__.
* Also FIX  Allow payments in __PriceUnit__ other than currency (!).
* Also FIX Add __ruleStepResults \ RuleStep__ to __SalesTransaction__.
* Also FIX Type of __Transaction__ \ __Amount__  to be _currencyType_ not _distanceType_.
* Also add a   __Narrative__ text element on __RuleStepResult__.
* Also add __UnitDimension__ attribute to __PriceUnit__ with values _currency, distance, time, valueToken, other_.
* Also revise  __FarePrice__ element   to add __AmountWithResultsGroup__ and refactor  __FarePriceAmount__ groups to be clearer.
* Also revise __PriceRuleStepResult__:  add  new attributes __AdjustmentAmount__, __AdjustmentUnits__,  __RoundingRef__.
* NB this revises current sense of   __PriceRuleStepResult__ \ __Amount__.
* Also allow nesting of __FareTable__ column headings and rows.
* Add __RoundingStepRef__, and   __Narrative__ text elements.
* _Updates to xml schema_:
    * netex_farePrice_support.xsd
    * netex_farePrice_version.xsd
    * netex_fareTable_support.xsd
    * netex_fareTable_version.xsd
    * netex_salesTransaction_version.xsd
* _Updates to xml examples_:
    * examples\rail\tariffs\Netex_era_distance_ro.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.13 NORWAY-100 *Part3-FARES*: Support VAT (and other tax)  categories.
* Add __TypeOfPricingRule__  element.
* Also FIX  add missing (!) relationship  __ruleStepResults \ RuleStep__ on  __SalesTransaction__.
* Also FIX  Allow payments in __PriceUnit__ other than currency (!).
* Also FIX Add __ruleStepResults \ RuleStep__ to __SalesTransaction__.
* Also FIX Type of __Transaction__ \ __Amount__  to be _currencyType_ not _distanceType_.
* Also add a   __Narrative__ text element on __RuleStepResult__.
* Also add __UnitDimension__ attribute to __PriceUnit__ with values _currency, distance, time, valueToken, other_.
* Also revise  __FarePrice__ element   to add __AmountWithResultsGroup__ and refactor  __FarePriceAmount__ groups to be clearer.
* Also revise __PriceRuleStepResult__:  add  new attributes __AdjustmentAmount__, __AdjustmentUnits__,  __RoundingRef__.
* NB this revises current sense of   __PriceRuleStepResult__ \ __Amount__.
* Also allow nesting of __FareTable__ column headings and rows.
* Add __RoundingStepRef__, and   __Narrative__ text elements.
* _Updates to xml schema_:
    * netex_farePrice_support.xsd
    * netex_farePrice_version.xsd
    * netex_fareTable_support.xsd
    * netex_fareTable_version.xsd
    * netex_salesTransaction_version.xsd
* _Updates to xml examples_:
    * examples\rail\tariffs\Netex_era_distance_ro.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.12 EURA-40 *Part3-FARES*:  Add integrity  constraints for  new elements.
* Elements __Subscribing__, __TypeOfPaymentMethod__, __TypeOfFareStructureFactor__, __TypeOfFareStructureElement__, __TypeOfPricingRule__.
* Also drop some spurious selectors.
* Add constraint for __SupplementToFareProductRef__.
    * _Updates to xml examples_:
    * netex_publication_support.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.03.12 NORWAY-100 *Part3-FARES*: Add __ReservationType__ to __Reserving__ usage parameter.
* With values _autoAssigned_, _seatMap_  and _openSeating_.
* _Updates to xml schema_:
    * netex_usageParameterBooking_support.xsd
    * netex_usageParameterBooking_version.xsd
* _Updates to xml examples_:
    * examples\standards\fxc\uk_fxc_trip_Metrobus_1.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.12 NORWAY-102 *Part3-FARES*:   Add  new enum values to __Exchanging__ \  __ExchangeableTo__.
* Values _upgradeToSpecifiedFare_, _downgradeToSpecifedFare_, _equivalentProduct_ (already have a _changeGroupSize_ value).
* Also add new _purchaseGracePeriod_ (i.e. afterPurchaseWindow)    enum values to  __Reselling  \  ResellWhen__.
* _Updates to xml schema_:
    * netex_usageParameterAfterSales_support.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.12 NORWAY-105 *Part3-FARES*:   Add new __MinimumDuration__  attribute to __TimeInterval__.
* Also fix __TypeOffareStructureFactor__ on __GeograohicalStructreFactor__.
* _Updates to xml schema_:
    * netex_timeStructureFactor_version.xsd
    * netex_geographicalStructureFactor_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.12 EURA-84 *PART1-ND*   Add default __PaymentMethods__, to __Lines__.
* add xml groupwith __PaymentMethods__, __TypesOfPaymentMethods__   and __PurchaseMoments__ attributes.
* Add to __Network__, __GroupOfLines__, and __Line__.
* Also add  _cashExactChangeOnly_ to values for __PaymentMethods__.
* _Updates to xml schema_:
    * netex_travelRights.xsd
    * netex_line_version.xsd
* _Updates to xml examples_:
    * examples\standards\fxc\uk_fxc_trip_Metrobus_1.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.12 UK-45  *Part3-FARES*:  Add  constraint mechanism  to Entitlements.
* This so that supplements and dependent products can be required to have same parameters.
* Add constraint elements to   __EntitlementRequired__, __EntitlementGiven__.
* Add constraint elements to   __SalesOfferEntitlementRequired__, __SalesOfferEntitlementGiven__.
* _Updates to xml schema_:
    * netex_usageParameterEntitlement_support.xsd
    * netex_usageParameterEntitlement_version.xsd
    * netex_salesOfferPackageEntitlement_support.xsd
    * netex_salesOfferPackage_version.xsd
* _Updates to xml examples_:
    * examples\standards\fxc\uk_fxc_pass_Metrobus_metrorider.xml
    * exaamplesstandards\fxc\uk_fxc_addon_HSP_plusbus.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.12 NORWAY-99  *Part3-FARES*:  Change cardinality of __SupplementProduct__.
* Change __SupplementProduct__ / __SupplementToFareProductRef__ cardinality   from _0:1_ to _0:*_.
* Also add  missing constraint for __SupplementTofareProductRef__.
* _Updates to xml schema_:
    * netex_fareProduct_supplement.xsd
    * netex_fareProduct_version.xsd
    * netex_publication_version.xsd
* _Updates to xml examples_:
    * examples\standards\fxc\uk_fxc_pass_Metrobus_metrorider.xml
    * exaamplesstandards\fxc\uk_fxc_addon_HSP_plusbus.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 NORWAY-98  *Part3-FARES*:  NORWAY-98 Add new  value _activation_ to __UsageTriggerEnumeration__ for __UsageValidityPeriod__.
* Also add  _Deregistration_ value to __UsageEnd__ enumeration
* Also and annototation comments.
* _Updates to xml schema_:
    * netex_usageParameterTravel_support.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 NORWAY-97 *Part3-FARES*:  : Add new values to __UserProfile \ UserType__,
* Values: _student, schoolPupil, youngPerson, military, disabled, disabledCompanion,  employee, jobSeeker_.
* _Updates to xml schema_:
    * netex_user_support.xsd
* _Updates to xml examples_:
    * \examples\standards\fxc\uk_fxc_common_profile.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 EURA-87 *Part3-FARES*:  Support Partial Refunds of   Passes
* Add new enumeration values  _unused_ and _earlyTermination_ to __RefundType__ on __Reselling__.
* Add new __RefundPolicy__ attribute to __Refunding__ with enum values   _illness, death, redundancy, maternity, other, etc_
* Add new __RefundBasis__  atribute to __Refunding__  _unusedDays, unusedWeeks, unusedMonths, other_.
* Add new  __ExchangableFromPercentUse__ and __ExchangableUntilPercentUse__ attributes to __Reselling__.
* Add new enumeration value _withinSpecifiedWindow_  to __PurchaseWhen__  attribute on __Reselling__.
*  Add add new __EffectiveFrom__ attribute  to __Reselling__ with values _anytime, nextInterval, nextInstallment, never_.
* Add new __NoticePeriod__ to __Reselling__.
* Also UK-46- Add __typesOfPaymentMethods /TypeOfPaymentRef__ and move __PaymentMethods__ up hierarchy with new name (Old attribute on __Refunding__  deprecated)
* _Updates to xml schema_:
    * netex_usageParameterAfterSales_support.xsd
    * netex_usageParameterAfterSales_version.xsd
* _Updates to xml examples_:
    * netex_era_toc_uk.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 EURA-52, EURA40 *Part3-FARES*:  Support Suspension.
* Add _subscription_ enum value to __UsageValidityPeriodType__.
* Add __SubscriptionSuspensionPolicy__ attribute to __UsageValidityPeriod__ with enumeration   values:
    * _none_ - Suspension not allowed.
    * _forCertifiedIllness_ - Suspension allowed for illness.
    * _forParentalLeave_ - Suspension allowed for parental leave.
    * _forHoliday_ - Suspension allowed for Holiday.
    * _forAnyReason_ - Suspension allowed for any reason.
* _Updates to xml schema_:
    * netex_usageParameterTravel_support.xsd
    * netex_usageParameterTravel_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 EURA-72  *Part3-FARES*:   Improve __FareDemandType__ for direction constraints.
* Make  __StartTimeAtStop__  and __StartTime__ optional.
* Add new attribute StopUseConstraint__ to   __FareDemandType__ with values _arriving_. _departing_, _passingThrough_.
* _Updates to xml schema_:
    * netex_fareQualityFactor_support.xsd
    * netex_fareQualityFactor_version.xsd
* _Updates to xml examples_:
    * netex_era_toc_uk.xsd
    * Netex_101.21_TfL_GeographicFares_UnitZone_MultipleProduct.xml
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 CR-13  *PART1*:   Add _replacement_  value  to __LineType__ enumeration .
* _Updates to xml schema_:
    * netex_line_support.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 EURA-40 *Part3-FARES*:  Support Subscriptions.
* Add new  __Subscribing__ usage parameter.
* Add __SubscriptionRenewalPolicy__ attribute with enumeration   values:
    * _automatic_ - Renew automatcally at end of term.
    * _manual_ - Renew on request.
    * _automaticOnConfirmation_ - Confirm and renew automatically at end of subscription  term.
    * _none_ - No renewal allowed.
* Add __SubscriptionTermEnumeration__ attribute with enumeration  values:
    * _fixed_ - Subscription must be for a fixed term.
    * _variable_ - Subscription can be for  an arbitrary term
    * _openEnded_ - Subscription term is open ended.
* Also cf UK-46  Add new __TypeOfPayment__ method.
* Also Add __AutomatedUse__ attribute to __TypeofPaymentMethod__.
* Also Add _directDebit_ and bankTransfer_ values   to __PaymentMethod__ enumeration values.
* Also  __RESELLING__ parameter Add __typesOfPaymentMethods/TypeOfPaymentRef__ and move __PaymentMethods__ up hierarchy with new name (Old attribute on __REFUNDING__  deprecated)
* Also Add _unused_ and _earlyTermination_ to  __Refunding__ __RefundType__ enumeration.
* Also Add with specified window value to __PurchaseWhen__ enumeration attribute.
* Also EURA-90 Add a new attribute  __MaximumNumberOfFailToCheckOutEvents__  to __PenaltyPolicy__.
* _Updates to xml schema_:
    * netex_usageParameterCharging_support.xsd
    * netex_usageParameterCharging_version.xsd
    * netex_usageParameterAfterSales_support.xsd
    * netex_usageParameterAfterSales_version.xsd
    * netex_travelRights_support.xsd
    * netex_travelRights_version.xsd
    * netex_salesDistribution_support.xsd
* _Updates to xml examples_:
    * netex_91.1_Rail_RailCard_MultipleProducts.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 EURA-73  *Part3-FARES*:  Add new  __StartConstraintType__ attribute enumeration  for __UsageValidityPeriod__.
* Add __StartConstraintType__With enum values  _fixed_, _variable_, _fixedWindow_
* Also EURA-88 Flexible start window: Add new __FixedStartWindow__	attribute to __UsageValidityPeriod__ with contents
  __MaximumServicesBefore__. __FlexiblePeriodBefore__, __MaximumServicesAfter__, __FlexiblePeriodAfter__.
* _Updates to xml schema_:
    * netex_usageParameterTravel_support.xsd
    * netex_usageParameterTravel_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 UK-22  *Part3-FARES*:  Add new __PrivateCode__ attribute to __FarePrice__.
* Also UK-22 Add new __Description__ attribute to __FareProductPrice__.
* Also UK-22 Add new __InfoLinks__ attribute to __PriceableObject__.
* _Updates to xml schema_:
    * netex_farePrice_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 UK-55  *Part3-FARES*: Add new __TypeOfFareStructureElement__.
* Also	UK-89 Add new __TypeOfFareStructureFactor__.
* Also EURA-77 Fix: Corrections to __TypeOfFareProduct__.
* _Updates to xml schema_:
    * netex_fareStructureElement_support.xsd
    * netex_fareStructureElement_version.xsd
    * netex_fareStructure_support.xsd
    * netex_fareStructure_version.xsd
    * netex_fareProduct_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 UK-31 *FRAMEWORK*  Fix: to attribute names on __TypeOfFrame__.
* __TypeOfFrame__ Change data type on __ClassAttributeInFrame__ and __ClassRelationshipInFrame/Name__ attributes   from __NCName__ to __QNAME__.
* _Updates to xml schema_:
    * netex_versionFrame_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 EURA-77 *Part3-FARES*:  Add new relationship between  __FareProduct__ and __Tariff__.
* Add new __tariffs/TariffRef__  attribute to  __FareProduct__.
* _Updates to xml schema_:
    * netex_fareProduct_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 EURA-71 *Part3-FARES*:   Add new  _superOffPeak_ and _specialEvent_  enumeration values  to __FareDemandType__.
* _Updates to xml schema_:
    * netex_usageParameterBooking_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11 EURA-76 *Part3-FARES*:  Add __IsFeeRefundable__ attribute to __Reserving__.
* _Updates to xml schema_:
    * netex_usageParameterBooking_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.11  EURA-68 *Part3-FARES*:  Specify conditions for changing  group size.
* __Exchanging__ usage parameter __TypeOfExchange__ attribute: add new  enumeration  value _changeGroupSize_.
* Also __GroupTicket__ add new attribute __GroupSizeChanges__ with enum values _noChanges, free, charge, steppedCharge_.
* Also for __Refunding__ usage parameter,   add  new _changeOfGroupSize_  value  to __RefundType__ enumeration.
* _Updates to xml schema_:
    * netex_usageParameterAfterSales_support.xsd
    * netex_usageParameterEligibility_support.xsd
    * netex_usageParameterEligibility_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.10 UK-21 *Part3-FARES*:  Add  new __SalesOfferEntitlementGiven__ and __SalesOfferEntitlementRequired__  usage parameters.
*  Add as new package because __SalesOfferPackage__ dependencies are downstream from __FareProduct__.
* _Updates to xml schema_:
    * netex_salesOfferPackageEntitlement_support.xsd (new)
    * netex_salesOfferPackageEntitlement_version.xsd (new)
    * netex_salesOfferPackage_version.xsd
    * netex_all_objects_part3_fares_SD.xsd
    * netEx.SPP
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.10 EURA-42 *Part3-FARES*: Add __Currency__ to __PricingRule__ (NB this does not solve other aspects of CR.
* _Updates to xml schema_:
    * netex_calculationParameters_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.10 EURA-65  *Part3-FARES*:  Add new __SharedUsage__ attribute to __Transferability__  to specify whether multiple users may use a product at the same time.
* Add new enum for __SharedUsage__  with values _oneAtATime_, _severalAtATime_, _severalSpecifiedCompanionsAtATime_.
* _Updates to xml schema_:
    * netex_usageParameterAfterSales_support.xsd
    * netex_usageParameterAfterSales_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.10 EURA-75  *Part3-FARES*: Add new __Add TravelBillingPolicy__ attribute to __ChargingPolicy__.
* With enumerated values;  _billAsYouGo_ , _billOnThreshold_, _billAtFareDayEnd_, _billAtPeriodEnd_.
* _Updates to xml schema_:
    * netex_usageParameterCharging_support.xsd
    * netex_usageParameterCharging_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.10 UK-32 *Part3-FARES*: Add new __ResidenceType__ attribute to __ResidenceQualification__.
* With enumerated values;  _live_, _work_, _study_, _born_
* Also EURA-62:  Add new __CompanionRelationshipType__ attribute to __CompanionProfile__ with enumerated values _anyone, grandparent, parent, child, grandchild, colleague, family, legalRelative,   spouse, partner, colleague, teacher, pupil_.
* Also EURA-89 Add new enumeration value _birthCertificate_ to     __ProofOfIdentity__.
* _Updates to xml schema_:
    * netex_usageParameterEligibility_support.xsd
    * netex_usageParameterEligibility_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.10 EURA-53 *Part3-FARES*:   Add new __CappingRuleStartConstraintType__ attribute to __CappedFareProduct__ __CappingRule__ to state  if _fixed_ or _variable_.
* Also,  if _fixed_, specify a __startOnlyOn__ \ __DayType__, e.g. for day of week.
* _Updates to xml schema_:
    * netex_fareProduct_support.xsd
    * netex_fareProduct_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.10 EURA-67 *Part3-FARES*:    Add new _courier_ value to __FulfilmentMethodType__  enumerations.
* _Updates to xml schema_:
    * netex_salesDistribution_support.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.10 EURA-91 *Part3-FARES*:   Add new enumerated values _sameProductLongerJourney_ and _sameProductShorterJourney_ to __TypeOfExchange__ attribute on   __Exchanging__ usage parameter.
* _Updates to xml schema_:
    * netex_usageParameterAfterSales_support.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.10  EURA-87 *Part3-FARES*: Specify if start  of validity is _variable_ or _fixed_.
* Add new __StartConstraint__ attribute to __UsageValidityPeriod__  to  specify if start day  is _variable_ or _fixed_.
* Add new values _variable_ /  _fixed_ to  __UsageStartConstraintTypeEnumeration__.
* Add new  __startOnlyOn__  /  __DayType__ attribute so that any required day of week, day of month, month of year can be indicated.
* Add two XML groups to organise absolute and variable start time attributes.
* Also add new _enrolment_ and  _reservation_ enum values to __UsageTriggerEnumeration__.
* Also add new _eligibilityExpiry_  enum value to __UsageEndEnumeration__.
* Also EURA-94  Add new enumeration values _networks_, _operators_ and _countries_ to  type of step on  __StepLimit__.
* _Updates to xml schema_:
    * netex_usagwParameterTravel_support.xsd
    * netex_usageParameterTravel_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.10  UK-38 *Part3-FARES*:  Add new attributes __MinimumAccess__ and __MaximumAccess__ to __FareStructureElementinSequence__.
* _Updates to xml schema_:
    * netex_fareStructureElement_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.10 EURA-81 *Part3-FARES*:  Make relationship between __FareProduct__ and  __TypeOfFareProduct__ many-to-many.
* _Updates to xml schema_:
    * netex_fareProduct_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.10 UK-08 *FRAMEWORK* Add new attribute __LayerRef__  to __VersionFrame__ and to __TypeOfFrame__.
* _Updates to xml schema_:
    * netex_layer_support.xsd
    * netex_versionFrame_version.xsd

### 2019.03.10 UK-28 *Part3-FARES*: Add new attribute __CustomerAccountRef__ to  __FareContract__.
* _Updates to xml schema_:
    * netex_salesContract_version.xsd
    * netex_salesTransaction_version.xsd

### 2019.03.09 UK-12 *Part3-FARES*: Add  new attribute __GroupOfOperatorRef__  to __Tariff__ (ie make relationship many to many).
* _Updates to xml schema_:
    * netex_fareStructureElement_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.09 EURA-78 *Part3-FARES*: Allow more than one reference to a __GroupsOfSalesOfferPackageRef__  from a __SalesOfferPackage__ (i.e. make relationship many-to-many.)
* _Updates to xml schema_:
    * netex_salesOfferPackage_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.08 EURA-54 *Part3-FARES*: Add a seat reference to assignable parameters.
* Add a new module with __PassengerSeatingRef__.
* Also Add a  new attribute __PassengerSeatRef__  to __ServiceValidityParameterGroup__ of  __accessRightParamaterAssignment__.
* Also Add new  __TravelDocumentRef__ and  __RetailDeviceRef__ attributes to __SalesTransaction__.
* Also Fix: make __RetailingOrganisationRef__ an __OrganisationOperatorRefStructure__ rather than an __OperatorRefStructure__.
* _Updates to xml schema_:
    * netex_vehicleSeating_support.xsd (New)
    * netex_all_objects_reusable_components.xsd
* netex.spp
    * netex_accessRightParameter_version.xsd
    * netex_salesTransaction_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.08 EURA-43 *Part3-FARES*: Add new relationship to __FareZone__ to indicate who who manages it.
* Add new attributes to __FareZone__ ; __AuthorityRef__ / __OperatorRef__,   __GroupOfOperatorsRef__.
* _Updates to xml schema_:
    * netex_fareZone_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.08 EURA-51 *Part3-FARES*: Add new enumeration values to __RoundTripType__ ; _returnOut_, _returnBack_  so as to distinguish legs.
* _Updates to xml schema_:
    * netex_usageParameterTravel_support.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.08 PART2 UK-44, UK-69 *Part3-FARES*: Improve support for defining large tariffs in  modular fashion
* Add  new relationship  __groupsOfOperators/GroupsOfOperatorRef__  to __Network__.
    * Also __UseToExclude__   attribute to __GroupOfOperators__.
    * Also add new values  _flexible_ and _urban_ to __TypeOfLine__ enumeration.
    * Add new __UseToExclude__ flag to __GroupOfLines__.
    * Add new __UseToExclude__ flag to __GroupOfDistanceMatrixElements__.
* _Updates to xml schema_:
    * netex_line_support.xsd
    * netex_line_version.xsd
    * netex_transportOrganisation_support.xsd
    * netex_transportOrganisation_version.xsd
    * netex_distanceMatrixElementVersion_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.08  UK-14 *Part3-FARES*: Improvements to __FareZone__.
* Add new __ScopingMethod__  attribute to __FareZone__ with   values  _explicitStops_,   _implicitSpatialProjection_, _implicitSpatialProjection._
* UK-13 Add new  __ZoneTopology__ enumeration  values   _annular_,   _sequence_, _overlappingSequence_.
* UK-18 Specify  fare stages  on a   pattern: Add new __IsFareStage__ attribute to __FarePointInPattern__.
* EURA  Allow stops to be excluded from a routing.    Add new  __IsForbidden__ attribute  to __FarePointInPattern__.
* _Updates to xml schema_:
    * netex_fareZone_support.xsd
    * netex_fareZone_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.07 UK-46 *FRAMEWORK* & *Part3-FARES*: Add open   __PaymentMethod__ as first class object  so that user defined methods can be added.

* _Updates to xml schema_:
    * netex_travelRights_support.xsd
    * netex_travelRights_version.xsd
    * netex_salesDistribution_support.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.07 NJSK *Part3-FARES*: UK-74 Add new enumerations to __TariffBasis__;  _zoneToZone_, _pointToPoint_, _discount_.
* Also add documentation annotations   to existing annotations.
* _Updates to xml schema_:
    * netex_fareStructureElement_support.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.07 NJSK Fix *FRAMEWORK* Make __InfrastructurePointRef__ and __InfrastructureLinkRef__ abstract.
* _Updates to xml schema_:
    * netex_networkInfrastructure_support.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.03.07 NJSK-Fix *HOUSEKEEPING*  Delete spurious references in XMLSpy  _netext.ssp_  file.
* _Updates to other files_:
    * netex.spp
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.03.07  NJSK-Fix *FRAMEWORK* - Correct Type of __VersionFrameRef__ to be _VersionFrameRefStructure_ , correct substitution group on __ResourceFrameRef__ to be __VersionFrameRef__.
* _Updates to xml schema_:
    * netex_resourceFrame_version.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.03.07 EURA-40 *Part3-FARES*: Add support for  Subscriptions.
* Basic steps
    * Subscriptions add new values  _onlineAccount_  and _postal_ to enumerations  of __DistributionChannelType__.
    * Add _subscriptionOnly_, also _onCheckIn_, _inAdvanceOnly_, _beforeBoardingOnly_ , _onBoardingOnly_  to  __PaymentMoment__ enum.
    * Fix: add __PaymentMoment__ to __PurchaseWindow__.
* _Updates to xml schema_:
    * netex_salesDistribution_support.xsd
    * netex_travelRights_support.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.05 UK-24 *FRAMEWORK-RC*: & *Part3-FARES*: Add open   __PaymentMethod__ as first class object  so that user defined methods can be added.
* Add _ePayDevice_, _ePayAccount_ and _mileagePoints_ to __PaymentMethod__ enum
* _Updates to xml schema_:
    * netex_travelRights_support.xsd
    * netex_travelRights_version.xsd
    * netex_salesDistribution_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.05 UK-96 *FRAMEWORK-CC*: Add   __prerequisites__ relationship to __VersionFrame__.
* _Updates to xml schema_:
    * netex_versionFrame_version.xsd
* _Updates to examples_:
    * Many fares exampels updated to indicate prerequisites.
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.05 UK-09 *Part3-FARES*: Add __TypeOfTariffRef__  and __FareElementInSequenceRef__ to __TravelSpecification__  so that can  correctly specify choices.
* _Updates to xml schema_:
    * netex_salesTransaction_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.05 UK-19 *Part3-FARES-FP*: Fix __PriceGroup__ should be abstract.
* _Updates to xml schema_:
    * netex_farePrice_version.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-doane]

### 2019.03.05 NJSK-Fix *PART1*: Make alternative name and date visible on __Direction__.
* _Updates to xml schema_:
    * netex_route_version.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-done]

### 2019.03.05 UK-41 *Part3-FARES*: Revise __UserProfile__ to allow more than one enum values for __ProofOfEligibilty__.
* _Updates to xml schema_:
    * netex_usageParameterEligibility_support.xsd
    * netex_usageParameterEligibility_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.02 UK-18 *Part3-FARES*: Add values for __TypeOfInterval__.
* _Updates to xml schema_:
    * netex_geographicalStructureFactor_support.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]


### 2019.03.02 UK-80 *Part3-FARES*: Add  further values to __GenericParameterAssignment__,
__TypeOfConcessionRef__, __TypeOfUsageParameterRef__,  __VehicleType Ref__, __TypeOfLineRef__.
* _Updates to xml schema_:
    * netex_validityCondition_support.xsd
    * netex_accessRightParameter_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.02 UK-41 *Part3-FARES*: Add an additional functional operator to __GenericParameterAssignment__ to clarify use of groups.
* New values: _oneOf_ /  _someOf_/  _allOf_.
* Also correct documentation on relational operators.
* _Updates to xml schema_:
    * netex_validityCondition_support.xsd
    * netex_accessRightParameter_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.03.01 EURA-(nk) *Part3-FARES*: Add __DistanceMatrixInverseRef__ for backwards direction of reference. Revise constraints.
* _Updates to xml schema_:
    * netex_distanceMatriElement_support.xsd
    * netex_distanceMatriElement_version.xsd
    * netex_publication.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.02.28 EURA-10 *Part3-FARES*: Improve __CustomerPurchasePackage__.
* Fix correct case on __customerPurchasePackageRefs__.
* Allow  inlining of __CustomerPurchasePackages__ in a __FareContract__.
* _Updates to xml schema_:
    * netex_customerPurchasePackage_support.xsd
    * netex_customerPurchasePackage_version.xsd
    * netex_salesTransaction_version.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.02.21 UK-07  *Part3-FARES*: Allow __xxPriceRefs__ directly in  __FareTable__ / __cells__.
* Also allow __VersionOfObjectRef__ on  __FareTable__ __Row__ and __Column__.
* _Updates to xml schema_:
    * netex_fareZone_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.02.21 UK-20 *Part3-FARES*: Add contains relationship to __FareZone__.
* _Updates to xml schema_:
    * netex_fareZone_version.xsd
* _Updates to xml examples_:
* uk_fxc_trip_First_WoE_Line48_stage+Passses.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.02.21 UK-57 *Part3-FARES*: Add Allow list of __MachineReadable__  enumerations,
* Also add open ended __TypeOfMachineRedability__.
* _Updates to xml schema_:
    * netex_travelDocument_support.xsd
    * netex_travelDocument_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.02.21 UK-34 *Part3-FARES*: TRAVEL DOCUMENT  should not be in FARE FRAME  - remove.
* _Updates to xml schema_:
    * netex_travelDocument_version.xsd
    * netex_fareFame_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.02.21 UK-07 *Part3-FARES*: __FareTable__ - Allow direct containment of __FarePriceRef__.
* Also UK-23 Add __FareSectionRef__ to  __FareTable / specifics__
* _Updates to xml schema_:
    * netex_fareTable_version.xsd
* _Updates to xml examples_:Various to drop unecessary __cells__ wrapper tags
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.02.21 .No-Fix *PART2*: Reapply 1.09  Fix Merge in correction  to spelling of __AccountingTime__.
* NB This will break any existing documents that use __AccountingTime__.
* _Updates to xml schema_:
    * netex_duty_version.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.02.21 .No-Fix *Part3-FARES*:  Reapply 1.09  Fix up examples
* _Updates to xml examples_:  fare examples, Norway examples
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.02.21 NJSK-Fix *FRAMEWORK*  Make dummy types abstract __TransportOrganisation__ .
* _Updates to xml schema_:
    * netex_transportOrganisation_version.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.02.21 NJSK-Fix *FRAMEWORK* Reapply 1.09 Make __ValidityCondition__ etc visible   [xsd only]
* _Updates to xml schema_:
    * netex_travelRights.xsd
    * netex_trainElement.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.02.21 NJSK-Fix: *FRAMEWORK* Reapply 1.09 Constraint changes and further clean up constraints  [xsd only]
* Changes include:
    * (a) Fix keyref constraint on __TimingLinkInJourneyPattern_AnyVersionedKey__,   (Drop __DropFarePointInPattern__. __TimingTimingLinkInJournePattern__, __StopTimingLinkInJourneyPattern__).
    * (b) Fix keyref constraint on __ServiceLinkInJourneyPattern_AnyVersionedKey__ (Drop __xxxPoints__).
    * (c) Fix keyref constraint on __FarePointInPattern_AnyVersionedKey__ - Add __xxxPoints__.
    * (d) Fix keyref constraint on __LinkInJourneyPattern_AnyVersionedKey__ - Ddrop __xxxPoints__.
    * (e) Fix constraint __ServiceLinkInJourneyPattern_AnyVersionedKey__ drop bogus __ServiceService__ selector.
    * (f) Fix __FarePointInPattern__ Key
    * (g) Fix keyref constraint on StopPointInJourneyPattern - remove bogus __DeadRunInPattern__ and __ServiceStopPointInPattern__ selectors.
    * (h) Fix keyref constraint on TimingPointInPattern - remove bogus __DeadRunInPattern__ and __ServiceStopPointInPattern__ selectors.
    * (i) Fix uniqueness constraint on  __HeadwayJourneyGroup__ - drop __RhythmicalJourneyGroup__.
    * (j) Fix (again) __Constraints on SalesOfferPackage__ and __SalesOfferPackagePrice__.
    * (k) Fix keyref  __LinkInJourneyPattern_AnyVersionedKey__  correct  __LinkInPattern__ to __ServiceLinkInPattern__.
    * (l) Fix remove obsolete __ParkingTaxRate__ constraint
    * (m) Fix Reinstate integrity constraints on StopPointInJourneyPattern, etc  {NB THIS MAY CATCHE EXISTING ERRORS IN EXAMPLES].
    * (n) Fix Add  constraints on __SectionInSequence__. {NB THIS MAY CATCHE EXISTING ERRORS IN EXAMPLES].
    * (o) Revise key names to emphasise when key is ordered separate.
    * (b) Fix Make uniqueness of __PriceGroup__ and  __FareTable__.
* _Updates to xml schema_:
    * netex_publication.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.02.18 NJSK-Fix *FRAMEWORK* Correct data type of __LayerRef__ and substitution group on __Layer__  and __CellRef__
* NB dependencies need sorting out - move layer to core framework?
* _Updates to files_:
  * netex_layer_support.xml
  * netex_layer_version.xml
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.02.18 NJSK-Fix OTHER  update XML SPy & Oxygen project files [xsd only]
* _Updates to files_:
    * netex_layer_support.xml
    * netex_layer_version.xml
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.02.18 NJSK-Fix OTHER  update XML SPy & Oxygen project files [xsd only]
* _Updates to files_:
    * netex.spp
    * netex.spr
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.02.18  EXAMPLES - Add new  Fare examples [xsd only]

#### Rail fares
* Example: Distance rail tariff:
    * Netex_era_distance_ro.xml
* Example: Point to Point Multi-operator National tariff and  single operator regional products:
    * netex_era_toc_uk.xml
* Example: Cross-border National tariff :
    * netex_crossborder_de.xml
#### Bus fares
* Example: Zone-to-zone bus fares:
    * uk_fxc_trip_Metrobus_1.xml.xml
* Example: Zonal day & season pass fares:
    * uk_fxc_pass_Metrobus_metrorider.xml
* Example: Stage trip fares:
    * uk_fxc_trip_First_WoE_stage-distance_minimal1.xml
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.02.18 UK-006 *Part3-FARES*: - Add missing FARE TABLE  price references.
* Fix: Add __CellSpecificNetworkGroup__   to Fare Table Specifics,
* Fix: Add __TariffZoneRef , LineRef, FareZoneRef,  TariffRef,  LineRef, ScheduledStopPointRef__ and   __FareStructureElementInSequenceRef__. __SectionRef__ to  __CellSpecificNetworkGroup__,
* _Updates to xml schema_:
    * netex_fareTable_version.xsd
    * netex_stopPlace_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2019.01.11 1.09  NJSK-Fix *Part3-FARES*: Constraints.
* Fix: Correction to constraints
    1. Fix keyref constraint on __TimingLinkInJourneyPattern_KeyRef__ - drop __xxxPoints__.
    2. Fix keyref constraint on __ServiceLinkInJourneyPattern_AnyVersionedKey__ - drop __xxxPoints__.
    3. Fix keyref constraint on __FarePointInPattern_AnyVersionedKey__ - add __xxxPoints__.
    4. Fix keyref constraint on __LinkInJourneyPattern_AnyVersionedKey__ - drop __FarePointInPattern__.
    5. Fix constraint __ServiceLinkInJourneyPattern_UniqueBy_Id_Version_Order__ drop __ServiceServiceLinkInJourneyPattern__.
    6. Fix __FarePointInPattern__ Key constraint
* _Updates to xml schema_:
    * netex_publication.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2019.01.10 HOUSEKEEPING  Migrate to Github. Rename all  schema files to remove version numbers.
* _Updates to xml schema_:
    * All NeTEx files changed.
* Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2018.06.02  GITHUBBER  FRAMEWORK Add __Centroid__ to __GroupOfStopPlaces__.
* _Updates to xml schema_:
  * netex_stopPlace_version.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

----
## v1.0.9

### 2018.06.06  CR057 NJSK add URL to Priceable object.
* _Updates to xm  schema_: netex_farePrice_version-v1.1.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2018.06.02  1.09 *BUG* Fix __UsageParameterRef__  - should be abstract to prevent use  [xsd only]
* _Updates to xml schema_: netex_usageParameter_Support-v1.1.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2018.06.02 *BUG* Fix __ServiceDesignator__ & __JourneyDesignator__ - Make fromPoint value optional  .
* _Updates to xml schema_: netex_vehicleJourney_Support-v1.1.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]
  [DOCTODO] Also Add designator UML diagram to SPec

### 2018.06.02  1.10 *BUG* Fix Substitution group  __PointInJourneyPattern__.
* _Updates to xml schema_: netex_journeyPattern-v1.1.xsd
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2018.06.02 Add __ServiceDesignator__ to __GroupOfServicesMember__ [DOCTODO]
*  _Updates to xml schema_: netex_serviceJourney_Version-v1.1.xsd

### 2018.06.01 CR049 Rename  to align with Transmodel.  Fix case of names  [xsd only]
* TM6 Alignment: Rename __SalesPackage__ to __SalesOfferPackage__
    * Fix: Correct the camel casing of __GroupsOfsaleOfferPackages__ ==>  __groupsOfSaleOfferPackages__
    * Fix: Correct constraint names
* _Updates to xml schema_:
    * netex_SalesOfferPackage_version-v1.1.xsd
    * NeTEx_publication.xsd
    * NeTEx_publication_timetable.xsd	*
    *  Nx.xsd
* _Updates to examples_:
    * Netex_tap_tsi_B3+more.xml
    * Netex_tap_tsi_B2.xml
    * Netex_tap_tsi_B2-71.xml
    * Netex_tap_tsi_B2-1181.xml
    *  Netex_tap_tsi_B2-1180.xml
    * Netex_tap_tsi_tcvs_irt_1.xml
    * Netex_tap_tsi_B3.xml
    * Netex_tap_Train_Hotel_SalesPackage_2.xml
    * Netex_101.21_TflGeographicFares_UnitZone_MultipleProducts
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2018.03.20 1.09  CR047 Fix __SupplementToFareProductRef__.
* Fix _ResultStepIdType_[xsd only]
* _Updates to xml schema_:
    * netex_farePrice_version & netex_FarePrice_support
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2018.03.20 1.09  Fix Inheritance of __CompanionProfileRef__  to be a type of __UserProfileRef__  [xsd only]
* _Updates to xml schema_:
    * netex_usageParameterEligibility_support-v1.0
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2018.03.20  CR049 Rename  to align with Transmodel
* Renames and fixes
    * Fix Capitalisation  [xsd only] x
    * Fix Capitalisation of wrapper tags
    * TM Alignment: __salesOfferPackages__  should be lower ca.mel case.
    * TM Alignment: __salesOfferPackageElements__  should be lower camel case.
    * TM Alignment: __saleslesOfferPackageSubstitutions__ should be lower camel case.
    * TM Alignment: __salesOfferPackagePrices__ should be lower camel case
    * TM Alignment: __salesOfferPackageRefs__ should be lower camel case.
*  _Updates to xml schema_:
    * netex_SalesOfferPackage_support-v1.1.xsd
    * netex_SalesOfferPackage_version-v1.1.xsd
    * netex_FareTable_version-v1.1.xsd
    * nete_AccessRight_Parameters_version-v1.1.xsd
    * netex_FareProduct_version-v1.1.xsd
* _Updates to multiple Examples_.
* _Documentation Changes_:  [uml_diagram: NONE], [doc-NONE]

### 2018.03.20  CR049 Rename to align with Transmodel    [*uml:v96-nk4; doc:v39*]
* TM Alignment: Rename __PassengerContract__ ==> __FareContract___.
* TM Alignment: Rename __PassengerContractEntry__ ==> __FareContractEntry__.
* TM Alignment: Rename __PassengerContractSecurityListing__ ==> __FareContractSecurityListing__.
* TM Alignment: Rename __TypeOfPassengerContract__ ==> __TypeOfFareContract__.
* TM Alignment: Rename __TypeOfPassengerContractEntry__ ==> __TypeOfFareContractEntry__.
* _Updates to xml schema_:
    * netex_fareContract_support-v1.1.xsd
    * netex_fareContract_version-v1.1.xsd
    * netex_salesTransaction_support-v1.1.xsd
    * netex_salesTransaction_version-v1.1.xsd
    * netex_salesTransactionFrame_version-v1.1.xsd
    * netex_publication.xsd
    * netex_publication_timetable.xsd
* _Documentation Changes_:  [uml_diagram: done], [doc-done]

### 2017.12.20 CR049 Rename  to align with Transmodel [*uml:v96-nk4; doc:v39*]
* TM Alignment: Rename __SalesPackage__ ==> __SalesOfferPackage__.
* TM Alignment: Rename __SalesPackageElement__ ==> __SalesOfferPackageElement__.
* TM Alignment: Rename __SalesPackageSubstitition__ ==> __SalesOfferPackageSubstitition__.
* TM Alignment: Rename __TypeOfSalesPackage__ ==> __TypeOfSalesOfferPackage__.
* TM Alignment: Rename __SalesPackageSubstitition__ ==> __SalesOfferPackageSubstitition__.
* TM Alignment: Rename __GroupOfSalesPackages__ ==> __GroupOfSalesOfferPackages__.
* _Updates to xml schema_:
    * netex_salesPackage_support-v1.1.xsd ==>   netex_aalesOfferPackage_support--v1.1.xsd
    * netex_salesPackage_version-v1.1.xsd ==>   netex_aalesOfferPackage_version-v1.1.xsd

### 2017.12.20  Fix up fare examples

---
## v1.0.8

### 2017-12-01  Further revisions & Fixes for v1.1
* Fix: Add notice assignments to **GroupOfDistanceMatrixElements** [*uml:v96-nk3; doc:v38.04*]
    * netex_distranceMatrixLement_version-v1.1.xsd
* Fix: Move _alternativeTexts_ up hierarchy to **EntityInVersion** [*uml:v96-nk2; doc:v38.03*]
* Fix: Move **AlterativeName** to generic framework so Organisation can reference. [uml 96-nk2; doc done v38.03]
    * netex_organisation_version-v1.1.xsd
    * netex_all_objects_generic_version-v1.0.xsd
* Fix: Add **ContactDetails** to **Line** as per uml [*uml:v96-nk2; doc:v38.03*]
    * netex_line_version-v1.1.xsd
* Fix: Update uml diagram for **PropertyOfDay**, **Line** [*uml:v96-nk2; doc:v38.03*]
* Fix: cd  - **Place** should be typed **Place_VersionStructure**  [*uml:v96-nk2; doc:v38.03*]
    * netex_place_version-v1.1.xsd
* CR: Cr0019/Cr0013 correct type on  **DayOffSet**  on **CourseOfJourney** and **ReliefOpportunity**, **InterchangeRule**,     [*uml:v96-nk2; doc:v38.03*]
    * netex_vehicleService_version-v1.1.xsd
    * netex_coupledJourney_version-v1.1.xsd
    * netex_interchange-v1.1.xsd
* Fix: Add   **DayOffSet**  to JourneyMeeting  [*uml:v96-nk2; doc:v38.03*]
    * netex_interchange-v1.1.xsd
* CR: Cr0051: Add _infolinks_ to **GroupOfEnNtities** [*uml:v96-nk3; doc:v38.04*]
    * netex_groupin-v1.1.xsd

### 2017-11-08  Further revisions & Fixes for V1.1
* Fix: Add   **DayOffSet** to **JourneyPartCouple**  [*uml:v96-nk2; doc:v38.03*]
    * netex_coupledJourney_version-v1.1.xsd
* Fix: Correct spelling &  Allow multiple infolinks on **FareProduct** [*uml:v96-nk2; doc:v38.03*]
    * netex_fareProduct_version-v1.1.xsd
* Fix: Add _MobileApp_  to **MediaType** enumeration [*uml:v96-nk2; doc:v38.03*]
    * netex_travelDocumentSupport_support-v1.1.xsd
* Fix: Allow version of derived view id   [*xsd only*]
    * netex_responsibility_version-v1.1.xsd
* Fix: Allow **DistanceMatrixView** on *AccessRightParameter**   [*xsd only*]
    * netex_accessRightParameter_version-v1.1.xsd
* CR: CR0051 Allow *Line* and _documentlinks_ on **Tariff** [*uml:v96-nk2; doc:v38.03*]
    * netex_fareStructureElement_version-v1.1.xsd
* CR: CR0051 Add _map_ and _faresheet_ to **InfoLink** types [*uml:v96-nk2; doc:v38.03*]
    * netex_utilityTypes_v1.1.xsd
* CR: CR0051 Allow **Presentation** details on **TariffZone** [*uml:v96-nk2; doc:v38.03*]
    * netex_zone_version-v1.1.xsd
* Fix: Add _totalNumberParkingSpaces_  to **ParkingProperties** [*uml:v96-nk2; doc:v38.03*]
    * netex_ifopt_parking_version-1.1,xsd
* Fix: Update **Facility** - correct _nuisance_ to match XML[*uml:v96-nk2; doc:v38.03*]
    * netex_facility_support-v1.1.xsd
* CR: CR0049 Change **PiQuery** to **PiRequest** [*uml:v96-nk2; doc:v38.03*]
    * netex_salesTransaction_support-v1.1.xsd   (replaces 1.0)
* CR: CR0040  Rework to make **Section** a type of **LinkSequence**  [*uml:v96-nk2; doc:v38.03*]
    * netex_commonSection_support-v1.1.xsd ++
    * netex_commonSection_version-v1.1.xsd ++
    * netex_section_support-v1.1.xsd
    * netex_section_version-v1.1.xsd
    * netex_linkSequence_version-v1.1.xsd
    * netex_lineNetwork_version-v1.1.xsd
    * netex_fareZone_version-v1.1.xsd
* CR: CR0049 TM Change. Move _Description_ to supertype for **LinkSequence** [*uml:v96-nk2; doc:v38.03*]
    * netex_journeyPattern_version-v1.1.xsd
    * netex_journey_version-v1.1.xsd
    * netex_ifopt_navigationPath_version-v1.1.xsd
    * netex_ifopt_parking_version-v1.1.xsd

### 2017-10-10 Further revisions & Fixes

* Fix: Correct **FareStructureElement** to allow Multiple interval support,    Add timeIntervals & geographical intervals to fareElement,  Also allow inlining of DistanceMatrixElements [xml]
    * netex_FareStructureELement_version_-v1.1.xsd
    * netex_all_objects_part3_fares-v1.0.xsd
    * netex_all_objects_part3_fares_FS-v1.1.xsd
    * netex_accessRightParameter_version-v1.1.xsd
* Fix: **CustomerPurchasPeackageElement**   add **GeographicalIntervalRef** & **TimeIntervalRef** [*uml:v96-nk2; doc:v38.03*]
    * netex_CustomerPurchasePackage_version_-v1.1.xsd

* CR: CR0049	TM alignment
  (i) **CustomerPurchasePackage** element add **TypeOfTravelDocument** to **ProductValidityParametersGroup**   [*uml:v96-nk2; doc:v38.03*]
    * netex_accessRightParameter_version-v1.1.xsd

  (ii) Fix Add **TypeOfTravelDocument** to **FareTable** specifics   [*uml:v96-nk2; doc:v38.03*]
    * netex_fareTable_version-v1.1.xsd
    * etex_all_objects_part3_fares_FP-v1.1.xsd
    * netex_distanceMatrixElement_version-v1.0.xsd
      (iii) Add **TypeOfTravelDocument** to **FareFrame**  [*uml:v96-nk2; doc:v38.03*]
    * netex_travelDocument_version-v1.1.xsd

* Fix: NeTEx **FareFrame** had wrong reference 1.0  [*xsd only*]
    * netx_all_objects_part3_fares-v1.1.xsd
    * netex_fareFrame_version-v1.0.xsd
    * netex_all-v1.0.xsd
    *  netex_salesTransactionFrame-v1.1.xsd
* CR: CR0051  Misc small fix - **ParkingArea**  add **NumberOfBaysWithRecharging**,  **RechargingAvailable** [*uml:v96-nk2; doc:v38.03*]
    * netex_parkingTariff_version-v1.1.xsd
    * netex_siteFrame_version-v1.0.xsd
    * netex_ifopt_all_objects-v1.0.xsd
* CR: CR0051- **LostPropertyService**:  add **KeptForDuration**.  **LeftLuggage addMaximumDuration**    [*uml:v96-nk2; doc:v38.03*]
    * netex_ifopt_localService_version-v1.1.xsd
    * netex_ifopt_localServiceCommercial_version-v1.0.xsd
    * netex_Ifopt_equipmentAll-v1.0.xsd
    * netex_assistanceBooking_version-v1.0.xsd

### 2017-08-17
* CR: CR0047 - **RailSubmode** add _AirportLink_  as rail submode [*uml:v96-nk2; doc:v38.03*]
    * netex_submode_version-v1.1.xsd
* FIX: Reorganise   project folders   [*xsd only*]
    * Split all_object_part3_fares into four sublists -FP, FS, AR, SD

### 2017-08-10 Align with TM6 Changes

* CR: CR0045 TM6: **GenericLoggable** support  **LogEntry**  [*uml:v96-nk2; doc:v38.03*]
  (i) Add generic **Loggable**.  Make **PassengerContractEvent** a type of **LogENtry**  [*uml:v96-nk2; doc:v38.03*]
    * netex_loggable_support-v1.1.xsd
    * netex_loggable_version-v1.1.xsd
    * netex_salesContract_support-v1.1.xsd

  (ii) Rename **PassengerContractEvent** to **PassengerContractEntry**  NB not back compatible for **TypeOfPassengerContractEvent**[*uml:v96-nk2; doc:v38.03*]
    * netex_salesContract_support-v1.1.xsd

  (iii) Add Support for **SecurityLists** & **WhiteLists*** , revise use of **lacklist**.  NB this is functionally, but not syntactically backwards compatible.  [*uml:v96-nk2; doc:v38.03*]
    * +netex_securityList_support-v1.1.xsd
    * +netex_securityList_version-v1.1.xsd
    * netex_salesContract_support-v1.1.xsd
    * netex_salesContract_version-v1.1.xsd
    * netex_travelDocument_support-v1.1.xsd
    * netex_travelDocument_version-v1.1.xsd
    * netex_retailConsortium_support-v1.1.xsd
    * netex_retailConsortium_version-v1.1.xsd
    * netex_salesTransactionFrame_version-v1.1.xsd

  (iv) Add **CustomerPurchasePackage** support  [*uml:v96-nk2; doc:v38.03*]
    * allObjects_part3
    * ++ netex_customerPurchasePackage_support-v1.1.xsd
    * ++ netex_customerPurchasePackage_version-v1.1.xsd
    * netex_salesTransactionFrame_version-v1.1.xsd

  (v) Add **CustomerAccount**, **CustomerAccountStatus**, **TypeOfCustomerccount**  [*uml:v96-nk2; doc:v38.03*]
    * netex_salesContract_support-v1.1.xsd    umlp
    * netex_salesContract_support-v1.1.xsd    umlp

  (vi) Add **CustomerEligibility** [*uml:v96-nk2; doc:v38.03*]
    * ++   netex_customerEligibility_support-v1.1.xsd umlp
    * ++    netex_customerEligibility_version-v1.1.xsd umlp
* CR: CR00xx   Add **Presentation** including graphics to **AllowedLineDirection** [*uml:v96-nk2; doc:v38.03*]
    * netex_line_version-v1.1.xsd umlp

* CR: CR0040  Revise **Section**: Add **GeneralSection** distinct from **CommonSection**.   [*uml:v96-nk2; doc:v38.03*]
  Separate out section  from point and link package. NB not strictly compatible just for **Section** usedIn **LinkSequence**
    * netex_pointAndLinkSequence_support-v1.1.xsd  UMLcp
    * netex_pointAndLinkSequence_version-v1.1.xsd  UMLcp
    * netex_pointAndLink_support-v1.1.xsd UMLcp
    * netex_pointAndLink_version-v1.1.xsd UMLcp
    * netex_lineSection_version-v1.1.xsd UMLcp
    * ++netex_section_support-v1.1.xsd UMLcp
    * ++netex_section_version-v1.1.xsd UMLcp
* CR: CR0010 **QuayType** Add _BusPlatform_ enum value [*uml:v96-nk2; doc:v38.03*]
    * netex_ifopt_stopPlace_support-v1.1.xsd
* CR: CR0030	Add **DayOffsets** [u*uml:v96-nk2; doc:v38.03*]
    * netex_coupledJourney_version-v1.1.xsd UM p
    * netex_datedPassingTime_version-v1.1.xsd
    * netex_monitoredPassingTime_version-v1.1.xsd
    * netex_passingTimes_version-v1.1.xsd
* CR: CR0010 Add **JourneyPartPosition**  to **JourneyPart** [*uml:v96-nk2; doc:v38.03*]
    * netex_coupledJourney_support-v1.1.xsd
    * netex_coupledJourney_version-v1.1.xsd
* CR: CR014 Add **GroupOfLinesType** enum [*uml:v96-nk2; doc:v38.03*]
    * netex_line_support-v1.1.xsd
    * netex_line_version-v1.1.xsd
* CR: CR0047  Add support for tax to **FarePrice**: self ref on **PriceRule** & **StepResult** [*uml:v96-nk2; doc:v38.03*]
    * netex_farePrice_version-v1.1.xsd
    * netex_parkingTariff_support-v1.1.xsd
    * netex_parkingTariff_version-v1.1.xsd
