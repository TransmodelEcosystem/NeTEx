# DRT examples and explanations
We expanded for NeTEx 2.1 DRT in serious manner.

## Updates in NeTEX 2.1
- `FlexibleLine` is folded into `Line`. Be aware that an area-oriented services is now also a "line".
- There can now exist multiple `ServiceBookingArrangement` and related stuff in a `mobilityService`. There can now be also (multiple) `ServiceBookingArrangement` in a `Line`. So, it is not necessary to have a `MobilityService`only to put a `ServiceBookingArrangement`into it.
- `BookingNote` is now also an object that can be referenced and translated with `AlternativeText`. **TODO**
- `serviceBookingArrangements` can now accept all other elements to describe the services:
  - `ServiceBookingArrangement`: How to book
  - `ServiceCompetitiveCondition`: What to do and what not
  - `ServiceEligibilityCondition`: Who can use the service.
- We allow parametrised deep links, and we also support service discovery for the booking and price information.
- The interaction of such serviceBookingArrangements is additive. E.g. all elements are within their group connected by OR. E.g. you are a senior or a child you can use the service. Be aware that this MAY result in the need to split a line to do it properly.

## Types of demand responsive traffic (DRT)

Based on the [concept in Switzerland](https://www.oev-info.ch/sites/default/files/2024-07/Fachkonzept%20On-Demand_v2.1_en.pdf).

### Scheduled on-demand
The on-demand service serves the same stops as the normal service, but only 
on demand (travellers must book their journey in advance). Accordingly, this
can also be shown in the classic timetable.
For example: Only the first and last stops on a regular timetable are served, as 
a journey is only booked in advance at these stops.

(Demand)stops

They are registered in DiDok and are subject to all relevant 
regulations, laws, V580 rules etc. for public transport stops.
Fixed direction of travel: the vehicle generally moves in a fixed direction of 
travel. This means that an indicative timetable and connection protection can 
be defined.

Fixed sequence of stops/points

The order in which the stops or static stops 
are served is predefined. 

Fixed timetable

With a fixed direction of travel with a fixed sequence of 
stops/points, a fixed timetable can be defined. The times must be strictly adhered to (see also the comparison with the timetable below). 
Connections defined: The service plan defines which connections should be 
maintained on arrival and departure at a station or other junction. A (indicative) 
timetable is required to define a connection guarantee. 

Service plan

The service plan contains the timetable for the line-based on-demand transport services. 
Necessary information includes the journey number, days of service, route, arrival, 
departure and transit times at the operating points and the permitted speeds in the 
individual sections of the route. 
There are also various other attributes such as low-floor buses, bar trolleys, bicycle 
transport and the obligation to make reservations.

### Corridor
n-Demand Korridorverkehr (corridor transport) has Sammelstellen ("collection points") in addition to the on-demand stops of On-Demand Linienverkehr
(scheduled on-demand). This creates a corridor (i.e., visually, if you imagine 
horizontal boundaries above and below the "main route" in the figure above). 
The bus will still only travel to locations for which a journey has been booked 
in advance.
The on-demand stops and collection points can be described in a timetable 
as a logical sequence. Either a fixed timetable or an indicative timetable can 
be created. For example, the indicative timetable (for the figure above) could 

Type Definition

provide for the departure from the two Sammelstellen ("collection points") and 
three on-demand stops, which would serve all 5 locations. If there were only 
reservations for the on-demand stops, then only the on-demand stops would 
be served (i.e., as a line).
Note: If the sequence cannot be adhered to, a timetable is excluded and only 
an indicative timetable is possible.

Sammelstelle (collection points)

are defined by the on-demand provider 
and have a fixed designation and a fixed geo-localisation. However, they are 
not available in the DiDok or cannot be handled by it (according to the current 
status).

Richtfahrplan (indicative timetable)

With a fixed direction of travel, possible 
service times are defined for individual stops/points. An indicative timetable 
can be defined, even if the sequence of stops/points is not fixed. It does not 
necessarily have to be possible to adhere to an indicative timetable (with a 
single vehicle)

### Area-oriented
With on-demand Flächenverkehr (areal transport), any stopping points within 
a zone are served during predefined (zone) operating times. The booked journeys can be bundled by the operator (depending on the business model).
This service does not have a pre-planned timetable. Instead, the demand request generates an "ad hoc" journey with different routes and without a fixed 
route. This means that journey times can vary from journey to journey. 
For example, a person could request transport from any location (their own 
front door) to a bus stop and use a taxi to get there. If several journeys are 
booked to/from the same location, a kind of shared taxi/bus could be formed.
Any location: represent geo-coordinates at which a destination, intermediate 
or end point of a journey is located. Although these must be stored in the form 
of a log (e.g. for billing purposes), they do not have to be persisted in a data 
storage system. In particular, the geo-coordinates themselves are already 
uniquely defined and do not require any special technical processing.

These services do not have a pre-planned timetable with journeys, but operating times 
and a predefined service area. If stops or Sammelstellen ("collection points") are used, 
these must also be defined. In addition, rules (see below) must be specified. An "ad 
hoc" journey with individual journeys and without a fixed route is generated via the 
demand. The journey times can vary from journey to journey, with the aim of ensuring 
that the operators organise the most ideal pooling and journey schedules possible. 
Measuring quality in terms of punctuality in the conventional sense is only possible to 
a limited extent. It still needs to be checked what waiting times are acceptable for 
customers.
The description of the area-type ODV offer is provided as an offer plan with the following information:
- Service areas and possible subdivision into zones
- Public transport stops, collection points or addresses
- operating times
- Rules
  - Zone rules (e.g. restrictions for journeys between zones)
  - Stop rules (e.g. a stop may not be approached by regular traffic)
  - Competition rules (the journey must not run parallel to a regular bus)
  - Waiting rules 
  - Connection rules (e.g. for feeders)
  - Ordering and reservation rules 
  - Further rules

### Special case: Feeder/Distributor
- Feeder/Distributor: Some stops are defined and used for interchanges (e.g. school buses, late-night bringing passengers home from railway station)


### Special case: Hail and ride
**TODO**

### Special case: Mixed line
(e.g. within the village everywhere between village given stops)

### Special case: Pooling
In Transmodel POOLING is something different. For the time being we will NOT model it here.

## Diagram of relevant elements

```mermaid

classDiagram
    %% Base classes
    class BookingArrangement {
        <<abstract>>
    }

    class ServiceBookingArrangement {
        <<abstract>>
    }

    class MobilityService

    class ChauffeuredMobilityService {
        serviceBookingArrangements: ServiceBookingArrangement[]
    }

    ChauffeuredMobilityService --> BookingArrangement
    ChauffeuredMobilityService --|> MobilityService

    %% Inheritance
    ServiceBookingArrangement --|> BookingArrangement

    %% Line has multiple BookingArrangement through a container
    class Line {
        bookingArrangements: BookingArrangement[]
    }
    Line --> "0..*" ServiceBookingArrangement : bookingArrangements

    %% ServiceBookingArrangement specializations
    class ServiceCompetitiveCondition {
        RoutingConstraintInFrameGroup : group
        DistanceFromClassical : xsd:integer
        TemporalDistanceFromClasical : xsd:duration
        PenaltyDrivingTimeFactor : xsd:decimal
        PenaltyTransferTimeFactor : xsd:decimal
        WalkTimeFactor : xsd:decimal
        InterchangeBetweenFlexibleServicesAllowed: xsd:boolean
        InterchangeWithConventionalServicesallowed: xsd:boolean

    }
    class ServiceEligibilityCondition {
        UserProfile
        CommercialProfile
        ResidentialQualification
        CompanionProfile

    }

    ServiceCompetitiveCondition --|> ServiceBookingArrangement
    ServiceEligibilityCondition --|> ServiceBookingArrangement

    %% Inside ServiceEligibilityCondition: subelements serviceExclusions to different ServiceExclusion
    class ServiceExclusion

    ServiceEligibilityCondition --> "0..*" ServiceExclusion : serviceExclusions

    %% Examples of specific eligibility items
    class ResidentialQualification
    class CompanionProfile
    class CommercialProfile
    class UserProfile

    ServiceEligibilityCondition --> ResidentialQualification
    ServiceEligibilityCondition -->CompanionProfile 
    ServiceEligibilityCondition -->CommercialProfile 
    ServiceEligibilityCondition --> UserProfile 
    ServiceCompetitiveCondition --> RoutingConstraintInFrameGroup

    %% Connect MobilityService to ServiceBookingArrangement
    MobilityService --> "0..*" ServiceBookingArrangement : offers
```

## The new LineType
As mentioned FlexibleLine is gone. It is all in Line now. So the FlexibleLineType and the LineType are now in one.

We omit the classical part of LineType and focus on the relevant values.

| LineType                  | Explanation                                                                                                       |
|---------------------------|-------------------------------------------------------------------------------------------------------------------|
| flexible                  | Use this for fixed timetable, but when reservation for stops or the journey is needed                             |
| corridorService           | This is used for corridor services.                                                                               |
| mainRouteWithFlexibleEnds | Do not use this.                                                                                                  |
| flexibleAreasOnly         | Multiple areas are used. No fixed stops                                                                           |
| hailAndRideSections       | When there are hail and ride parts in your fixed scheduled ride.                                                  |
| fixedStopAreaWide         | Area but with fixed stops only                                                                                    |
| freeAreaAreaWide          | One free area where it stops everywhere.                                                                          |
| mixedFlexible             | Different concepts are used on the same line, but no part is fixed (e.g. in one area fixed stops, then corrridor. |
| mixedFlexibleAndFixed     | Used for some types of corridors. E.g. free within villages and fixed route between them                          |
| other                     | Do not use this.                                                                                                  |

## TypeOfFlexibleService
Is no longer to be used

| TypeOfFlexibleService         | LineType to use instead |
|-------------------------------|-------------------------|
| ch:1:TypeOfFlexibleService:L  | fixed                   |
| ch:1:TypeOfFlexibleService:A  | freeAreaAreaWide        |
| ch:1:TypeOfFlexibleService:Ö  | corridorService         |
|ch:1:TypeOfFlexibleService:Z| mixedFlexibleAndFixed   |
| ch:1:TypeOfFlexibleService:F | freeAreaAreaWide  |

## CollectionPoints

```
            <ValueSet id="ch:1:ValueSet:TypeOfPlace" version="any" nameOfClass="TypeOfPlace">
              <values>
                <TypeOfPlace id="ch:1:TypeOfPlace:regularStop" version="any">
                  <Name>regular stop</Name>
                </TypeOfPlace>
                <TypeOfPlace id="ch:1:TypeOfPlace:drtCollectionPoint" version="any">
                  <Name>DRT collection point</Name>
                </TypeOfPlace>
              </values>
            </ValueSet>
```
## "The rules"
What is really new is the extension of the rules part.
One main advantage now is that many rules can be included.

**NOTE**: Many of the rules are not amusing the consumers.


### The BookingArrangement: How to make a reservation / book
The relevant element is `ServiceBookingArrangement`.

There are three different ways to hand over to a booking service:
* Normal URL through `BookingUrl` or `bookingUrls/BookingUrl`.
* Through `bookingUrls/BookingDeepUrl?. There are parameters that are sent in a GET request (see list below).
* Through the service descriptor in `bookingUrls/BookingService`. For a list of services the end point information is delivered. Be aware you still need the necessary account informations and/or security protocol elements.

| Parameter for deep links | Description                                                                            |
|--------------------------|----------------------------------------------------------------------------------------|
| from                     | From where to go coordinates                                                           |
| to                       | Destination as coordinates                                                             |
| when                     | Datetime of start                                                                      |
| numPassengers            | Number of passengers                                                                   |
| numSuitcases             | Number of suitcases                                                                    |
| impairment               | If there is a handicap wheelchair / electricWheelshair / cognitive / visuel / auditive |
| note                     | Additional information                                                                 |

This also will provide more information for connections to booking services **TODO**

### Competition Rules
In some cases DRT is not allowed to compete in some ways with scheduled public transport.
We have a set of parameters that can be set in a `ServiceCompetitiveCondition`:
- Routing constraint: Restrictions in what the SERVICE is allowed to do in connection with other SERVICES. If not set, then the rules apply in general.
- Distance from classical: Distance in metres to the line/service or classical public transport in general. Builds geometric exclusion zones.
- Temporal distance from classical: Temporal distance to the SERVICE / transfer in the RoutingConstraint or classical public transport in general.
- Penalty transfer time factor: Factor to multiply the classical public transfer times with for the calculation of the dominance of the demand responsive traffic.
- Walk time factor: Factor to multiply walk time for the classical public transport to calculate if the classical public transport still should dominate the demand responsive traffic.
- Are interchanges with flexible and/or conventional services allowed.


```
<ServiceCompetitiveCondition id="sba2" version="1">
	<Description>Simple exclusion of time and distance from classical line based public transport. As no lines are mentioned, it is valid for all lines</Description>
	<DistanceFromClassical>200</DistanceFromClassical>
	<TemporalDistanceFromClassical>PT15M</TemporalDistanceFromClassical>
</ServiceCompetitiveCondition>
<ServiceCompetitiveCondition id="sba2a" version="1">
	<Description>For the classic_line 1 the temporal distance needs to be at least 30M</Description>
	<serviceExclusions>
		<ServiceExclusion id="se1" version="1">
			<LineRef ref="classic_line" version="1"/>
		</ServiceExclusion>
	</serviceExclusions>
	<TemporalDistanceFromClassical>PT30M</TemporalDistanceFromClassical>
</ServiceCompetitiveCondition>
<ServiceCompetitiveCondition id="sba2b" version="1">
	<Description>Area based DRT can be "slowed" down also in a different way. By penalising the time used. Otherwise, people are guided by trip planners at the first stop to the DRT, while the classic is more reliable. Also, a minimum drive and maximum drive are defined.</Description>
	<PenaltyDrivingTimeFactor>1.5</PenaltyDrivingTimeFactor>
	<PenaltyTransferTimeFactor>1.2</PenaltyTransferTimeFactor>
	<WalkTimeFactor>1.1</WalkTimeFactor>
	<MinimumDriveDuration>PT5M</MinimumDriveDuration>
	<MaximumDriveDuration>PT20M</MaximumDriveDuration>
</ServiceCompetitiveCondition>
<ServiceCompetitiveCondition id="sba10" version="1">
	<Description>This shows how the "Google"/NL way can be modeled. There we have the safe_duration_factor and the _safe_duration_offset. The formula is like this. SafeTravelDuration (seconds) = safe_duration_factor × DrivingDuration (seconds) + safe_duration_offset . Be aware that those calculations only provide guide lines for trip planners. The actual timing must come from the reservation/booking/purchase process.</Description>
	<PenaltyDrivingTimeFactor>1.5</PenaltyDrivingTimeFactor>
	<!-- used as the safe_duration_factor -->
	<PenaltyDrivingTimeOffset>PT60S</PenaltyDrivingTimeOffset>
	<!-- used as the safe_duration_offset -->
</ServiceCompetitiveCondition>
<ServiceCompetitiveCondition id="sba7" version="1">
	<Description>Defines between which services transfers are allowed.</Description>
	<InterchangeBetweenFlexibleServicesAllowed>true</InterchangeBetweenFlexibleServicesAllowed>
	<InterchangeWithConventionalServicesAllowed>true</InterchangeWithConventionalServicesAllowed>
</ServiceCompetitiveCondition>
<ServiceCompetitiveCondition id="sba8" version="1">
	<Description>A transfer restrictions at given "virtual" points. May also be a single area.</Description>
	<transferRestrictions>
		<TransferRestriction id="tr1" version="1">
			<BothWays>true</BothWays>
			<!-- we generelly suggest not to use BothWays -->
			<RestrictionType>cannotTransfer</RestrictionType>
			<!-- if no points are provided it is true for the whole trip. -->
			<FromPointRef ref="alphaville_airport" version="1"/>
			<ToPointRef ref="alphaville_centre" version="1"/>
		</TransferRestriction>
	</transferRestrictions>
</ServiceCompetitiveCondition>
```


### Eligibility Rules
We will use `ServiceEligibilityCondition` to describe the eligibility.
The eligibility can be based on:
- `UserProfile`: Social profile of the passenger, based on age group, education, profession, social status, gender etc.
- `CommercialProfile`: A category of users depending on their commercial relations with the operator (e.g. frequency of usage)
- `ResidentialQualification`: e.g. live, work, study, exchange, nonResident
- `CompanionProfile`: The number of characteristics (weight/volume of luggage), but here the CompanionRelationshipType is the important thing: e.g. child, family, dependent, carer)

```
<ServiceEligibilityCondition id="sba3" version="1">
	<ResidentialQualification id="rq1" version="1">
		<TopographicPlaceRef ref="CantonOfBerne" versionRef="1"/>
		<ResidenceType>live</ResidenceType>
		<MinimumDuration>P100D</MinimumDuration>
	</ResidentialQualification>
</ServiceEligibilityCondition>
<ServiceEligibilityCondition id="sba3" version="1">
	<CompanionProfile id="cp1" version="1">
		<Description>A profile for an accompanioning family member with a discount and a special price.</Description>
		<fareTables>
			<FareTableRef ref="specialfaretable" versionRef="1"/>
		</fareTables>
		<prices>
			<UsageParameterPrice id="upp1" version="1">
				<IsAllowed>true</IsAllowed>
			</UsageParameterPrice>
		</prices>
		<CompanionRelationshipType>family</CompanionRelationshipType>
		<MinimumNumberOfPersons>1</MinimumNumberOfPersons>
		<MaximumNumberOfPersons>1</MaximumNumberOfPersons>
		<DiscountBasis>discount</DiscountBasis>
	</CompanionProfile>
</ServiceEligibilityCondition>
<ServiceEligibilityCondition id="sba3a" version="1">
	<CompanionProfile id="cp2" version="1">
		<Description>A profile for an accompanioning carer for free</Description>
		<CompanionRelationshipType>carer</CompanionRelationshipType>
		<MinimumNumberOfPersons>1</MinimumNumberOfPersons>
		<MaximumNumberOfPersons>1</MaximumNumberOfPersons>
		<DiscountBasis>free</DiscountBasis>
	</CompanionProfile>
</ServiceEligibilityCondition>
<ServiceEligibilityCondition id="sba4" version="1">
	<CommercialProfile id="cp2" version="1">
		<Description>**TO BE DISCUSSED**</Description>
		<ConsumptionUnits>2</ConsumptionUnits>
	</CommercialProfile>
</ServiceEligibilityCondition>
<ServiceEligibilityCondition id="sba5" version="1">
	<UserProfile id="up1" version="1">
		<Description>Must be of a certain age to use the service</Description>
		<MinimumAge>65</MinimumAge>
	</UserProfile>
</ServiceEligibilityCondition>
<ServiceEligibilityCondition id="sba6" version="1">
	<UserProfile id="up2" version="1">
		<Description>Must be a child of a given age, female and must have a student card (e.g. for a school bus).</Description>
		<UserType>child</UserType>
		<MinimumAge>4</MinimumAge>
		<MaximumAge>12</MaximumAge>
		<LocalResident>true</LocalResident>
		<GenderLimitation>femaleOnly</GenderLimitation>
		<ProofRequired>studentCard</ProofRequired>
	</UserProfile>
</ServiceEligibilityCondition>
```

## Examples 

### Regular line that runs and stops only when there are reservations.
- LineType="flexible"
- [XML](./CH_DRT_Line_Based_Reservation.xml)
### Area oriented with fixed CollectionPoints
In the Gotthard area mybuxi is providing services from CollectionPoints that can change a lot. CollectionPoints near railway stations are stable.

- LineType="fixedStopAreaWide"
- [XML](./CH_DRT_Area_mybuxi.xml)
- [Example ENTUR](KOL_KOL-FlexibleLine-a318c9ea-bae0-49da-8356-f4820e1d9cdd_9955_HentMeg---Sauda.xml)

### A mixed line with regular parts on area-oriented parts
- LineType="mixedFlexible"
- [XML](SKY_SKY-FlexibleLine-9ef2772d-b2b5-4b3a-935e-32d49ff6576e_Samnanger-ytre.xml)

## NeTEx to GTFS-Flex hints
This chapter deals with mapping NeTEx to GTFS-Flex.

### Things to use in GTFS-Flex
Important are:
- Areas
- FlexibleTrips
- BookingRules

`stop_times.txt`: Extended and modified file to include time-windows that a vehicle picks up and drops off at stops or location groups/areas

`booking_rules.txt`: new file that defines the booking rules / requirements that must be met for a successful booking.

`locations.geojson`: hat allows defining Zones using Polygons and MultiPolygons (for Zones with “holes”). 

`locations_groups.txt`: New files to allow grouping of stops which allow predetermined groups of these features to be specified on individual rows of stop_times.txt. This file specifically defines the group (similar to `areas.txt`).

`location_group_stops`: New files to allow grouping of stops which allow predetermined groups of these features to be specified on individual rows of stop_times.txt.  This file specifically defines the mapping of the groups from location_groups to stops (similar to `stop_areas.txt`). 

### How to model `safe_duration_factor` and `safe_duration_offset` 
From https://github.com/google/transit/commit/4ba262f50a6a355f6c849aaf757a9d1b4ef88722 


Current definition:
> Together, `safe_duration_factor` and `safe_duration_offset` allow an estimation of the longest amount of time a rider can expect the on-demand trip to take, for 95% of cases. <br><br> Data consumers are expected to use `safe_duration_factor` and `safe_duration_offset` to make the following calculation:<br><br> `SafeTravelDuration (seconds) = safe_duration_factor × DrivingDuration (seconds) + safe_duration_offset (seconds)`<br><br>where `DrivingDuration` is the time it would take a private car to travel the distance being calculated for the on-demand service, and `SafeTravelDuration` is the longest amount of time a rider can expect the on-demand trip to take. <br><br>This calculation should only apply to the portion of a trip that is on-demand. If a service is a deviated-fixed service, or if a rider trip includes a transfer from an on-demand to a fixed-route service, the duration of the fixed-route portion of the trip should be calculated according to the `departure_time` and `arrival_time` fields.<br><br>Empty values for `safe_duration_factor` and `safe_duration_offset` are considered as `1.0` and `0`, respectively.

In NeTEx you use: 

```
<ServiceCompetitiveCondition id="sba10" version="1">
	<Description>This shows how the "Google"/NL way can be modeled. There we have the safe_duration_factor and the _safe_duration_offset. The formula is like this. SafeTravelDuration (seconds) = safe_duration_factor × DrivingDuration (seconds) + safe_duration_offset . Be aware that those calculations only provide guide lines for trip planners. The actual timing must come from the reservation/booking/purchase process.</Description>
	<PenaltyDrivingTimeFactor>1.5</PenaltyDrivingTimeFactor>
	<!-- used as the safe_duration_factor -->
	<PenaltyDrivingTimeOffset>PT60S</PenaltyDrivingTimeOffset>
	<!-- used as the safe_duration_offset -->
</ServiceCompetitiveCondition>
```

## Model things from HRDF
The following relevant things in HRDF can be modeled in NeTEx already:

| HRDF feature | Explanation | NeTEx |
| -- | -- | -- |
|need for reservation | - | with `BookingArrangement` or `ServiceReservationFacilityType` set to `reservationsCompulsaory`|  
| no bicyles allowed | - | `LuggageCarriageType`set to `noCycles`|  
| additional fare necessary | - | `UicTrainRateEnum` set to `supplement` |  
| `*R * U 5` | additional time for transfer at stop | `ServiceCompetitiveCondition/transferRestrictions/TransferRestriction/TransferDelay` |  
| `*R *DT 14 14`| no competition to classical line |   
`ServiceCompetitiveCondition/TemporalDistanceFromClassical` |  
| `*SS *FAT 00 30` | Minimal-maximal drive duration. | `ServiceCompetitiveCondition/MinimumDriveDuration` and `ServiceCompetitiveCondition/MaximumDriveDuration` |

## Sources
- Definition of GTFS-Flex: https://gtfs.org/community/extensions/flex/
- Description, how it was done in Switzerland:
  - https://opentransportdata.swiss/en/cookbook/timetable-cookbook/gtfs-flex/
  - https://www.oev-info.ch/sites/default/files/2024-04/gtfs_profil_switzerland_version_0_16.pdf?