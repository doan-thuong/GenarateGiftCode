from enum import Enum

class StatusMail(Enum):
    CanOpen = 0
    Opened = 1

class StatusRewardMail(Enum):
    CanClaim = 0
    Claimed = 1
    NoReward = 2

class MailComponent:
    # Server booster
    TITLE_SERVER_BOOOSTER ="Server Booster Rewards!"
    DES_SERVER_BOOOSTER = "Greetings, Kings!\nThank you for supporting the Nightfall Discord server. Here’s a small gift from us—wishing you victorious battles ahead!"
    
    # mail trả quà bình thường khi gặp lỗi
    TITLE_COMPENSATION_REWARD ="Compensation Reward"
    DES_COMPENSATION_REWARD = "Hello Player,\nPlease accept this reward as compensation for any inconvenience you’ve experienced. Enjoy!\n— Game Support Team"
    
    # mail xin lỗi vì lỗi game khiến user chưa nhận được reward
    TITLE_MISSING_REWARD = "Apology for Missing Reward"
    DES_MISSING_REWARD = "Hello Player,\nWe’re sorry for the issue that caused you to miss your reward. Please accept this compensation as an apology.\nThank you for your understanding!"

class TableName:
    MAIL_BOX = "mail_box"
    BLACKLIST = "blacklist_device"
    DAILY_CHALLENGE_TICKET = "daily_challenge_ticket"
    DAILY_CHALLENGE_PACK = "daily_challenge_weekly_pack"
    PLAYER = "player_info"

class ColunmName:
    device_or_uid = "device_or_uid"
    player_id = "player_id"
    uid = "uid"
    device_id = "device_id"

class MoneyType:
    Gold = 0
    Gem = 1
    Stamina = 2
    AdventureTicket = 3
    DailyChallengeCoin = 5
    NormalKeyItemKey = 7
    GoldenItemKey = 8
    DailyChallengeTicket = 9
    GoldenCardKey = 10

    Chip = 11
    SkipTicket = 12
    CampaignStar = 13
    WeaponScroll = 14
    ArtifactScroll = 15
    MountScroll = 16
    HeroScroll = 17
    QuestGrowthFundPoint = 21
    DailyChestPoint = 22
    Silver = 23
    RandomScrollItem = 24
    WeekChestPoint = 25
    GuildBossTicket = 26
    GuildCoin = 27
    GuildExp = 28
    GuildPoint = 29
    BuildingSetToken = 30
    HiddenReward = 302
    Ads = 102
    IAP = 103
    PremiumCardSlot = 104

    RandomGem = 301

    RemoveAds = 400
    GameSpeedX2 = 401
    GameSpeedX3 = 402
    CoinX2 = 403
    CoinX3 = 404
    X2RewardAdventure = 405
    X2SpeedGateAdventure = 406
    XPlayReward = 407
    DailyGem = 408
    DailyEquipmentKey = 409
    DailyCardKey = 410
    DailyStamina = 411
    BonusCampaign = 412
    BonusAdventure = 413
    BonusIdleTaxLifetime = 414
    BonusMaxStamina = 415
    XLuckyWheelReward = 416
    BonusMaxIdleTax = 417
    FreeDoubleReward = 418
    XDailyDealReset = 419
    BonusIdleTax = 420
    DailyDailyChallengeCoin = 421
    DailyChallengeQuestBonusX = 422
    EasterEggDailyDice = 423

    RandomEquipmentCommon = 500
    RandomEquipmentRare = 501
    RandomEquipmentEpic = 502
    RandomEquipmentUnique = 503
    RandomEquipmentLegendary = 504
    RandomEquipmentDivine = 505

    RandomWeaponCommon = 510
    RandomWeaponRare = 511
    RandomWeaponEpic = 512
    RandomWeaponUnique = 513
    RandomWeaponLegendary = 514
    RandomWeaponDivine = 515

    RandomArtifactCommon = 520
    RandomArtifactRare = 521
    RandomArtifactEpic = 522
    RandomArtifactUnique = 523
    RandomArtifactLegendary = 524
    RandomArtifactDivine = 525

    RandomMountCommon = 530
    RandomMountRare = 531
    RandomMountEpic = 532
    RandomMountUnique = 533
    RandomMountLegendary = 534
    RandomMountDivine = 535

    RandomHeroCommon = 540
    RandomHeroRare = 541
    RandomHeroEpic = 542
    RandomHeroUnique = 543
    RandomHeroLegendary = 544
    RandomHeroDivine = 545

    RandomCardCommon = 600
    RandomCardRare = 601
    RandomCardEpic = 602
    RandomCardUnique = 603
    RandomCardLegendary = 604
    RandomCardDivine = 605

    RandomPetCommon = 650
    RandomPetRare = 651
    RandomPetEpic = 652
    RandomPetUnique = 653
    RandomPetLegendary = 654
    RandomPetDivine = 655
    SelectWeaponUniqueS = 656
    SelectArtifactUniqueS = 657
    SelectMountUniqueS = 658
    SelectHeroUniqueS = 659

    CandyCone = 701
    ChristmasSocks = 702

    ChristmasPoint = -22222

    EasterEggDice = 703
    EasterEggGrowthFundPoint = 704

    EasterEggPoint = -33333

    EasterEggAutoDice = 706
    EasterEggX3Speed = 707
    EasterEggExchangePoint = 708
    CardExchangePoint = 18
    TrialRemoveAds = 709
    TrialGameSpeedX2 = 710
    GuildActivityPoint = 809

    EasterEggReskinAutoDice = 712

    EasterEggReskinX3Speed = 713
    EasterEggReskinExchangePoint = 714
    EasterEggReskinDice = 715
    EasterEggReskinGrowthFundPoint = 716
    EasterEggReskinDailyDice = 717

    PetEgg = 718

    PetFood = 719
    PetPassiveStone = 720
    PetPassiveLockStone = 721

    LuckyBallGrowthFundPoint = 723

    LuckyBallSilverTicket = 724
    LuckyBallGachaChip = 725
    LuckyBallDailyGachaChip = 726

    LuckyBallSpecialBall = 727

    LuckySpinGachaChip = 728
    LuckyBallPremiumTicket = 729

    LuckyBallMiniGamePetCard = 730

    LuckyBallMiniGameBreakEgg = 731
    LuckyBallMiniGameSlotMachine = 732

    MidAutumnFishingLure = 733

    MidAutumnGrowthFundPoint = 734

    MidAutumnMiniGameMysteryBox = 735

    MidAutumnMiniGameBreakPot = 736
    MidAutumnMiniGameSlotMachine = 737
    MidAutumnFishingBreak = 738
    MidAutumnFishingRodEpic = 739
    MidAutumnFishingRodVip = 740
    MidAutumnMoonCake = 741
    MidAutumnLantern = 742
    MidAutumnFishRodBenefit0 = 743
    MidAutumnFishRodBenefit1 = 744
    MidAutumnFishRodBenefit2 = 745

    HalloweenGrowthFundPoint = 746

    HalloweenPickaxe = 747
    HalloweenBoosterRadar = 748
    HalloweenBoosterDynamite = 749
    HalloweenMinerTicket = 750
    HalloweenPickaxeDaily = 751
    HalloweenBenefitMaxPickaxeBonus = 752
    HalloweenBenefitAutoMining = 753
    HalloweenPumpkin = 754