// Game descriptions for tooltip display
const gameDescriptions = {
  // Pixel Games
  'basket-random': 'Experience hilarious basketball action with unpredictable physics! Basket Random features quirky characters with floppy movements and random court environments. Score baskets while dealing with wobbly controls, changing weather conditions, and gravity-defying moments. Perfect for quick fun sessions with friends or solo challenges.',
  
  'big-tower-tiny-square': 'Navigate through a massive tower filled with deadly traps and precise platforming challenges! This pixel-perfect adventure requires quick reflexes and determination as you guide a tiny square through increasingly difficult levels. Each death teaches you something new in this addictive precision platformer.',
  
  'boxing-random': 'Step into the ring for chaotic boxing matches with unpredictable physics! Control wobbly boxers in various arenas, from rooftops to icy surfaces. The random elements keep every fight fresh and hilarious, making it perfect for competitive multiplayer sessions or single-player tournaments.',
  
  'crossy-road': 'Cross busy roads, rivers, and train tracks in this endless arcade adventure! Guide your character through increasingly challenging obstacles while collecting coins and unlocking new characters. The voxel art style and simple one-touch controls make it instantly addictive.',
  
  'drift-boss': 'Master the art of drifting in this minimalist racing game! Keep your car on the winding track by perfectly timing your drifts around sharp corners. The longer you survive, the faster and more challenging it becomes. Simple controls, endless gameplay, and satisfying drift mechanics.',
  
  'drive-mad': 'Navigate through crazy obstacle courses with realistic physics! Drive various vehicles through loops, jumps, and mechanical contraptions while keeping your cargo safe. Each level presents unique challenges that test your driving skills and patience in this physics-based puzzle racer.',
  
  'park-out': 'Solve parking puzzles by moving cars in the correct sequence! This brain-teasing game challenges your logical thinking as you figure out how to get specific cars out of crowded parking lots. With hundreds of levels, each puzzle requires careful planning and strategic moves.',
  
  'retro-bowl': 'Lead your football team to championship glory in this nostalgic sports simulation! Manage your roster, call plays, and control the action on the field. The retro pixel art style combined with deep gameplay mechanics creates an authentic old-school football experience.',
  
  'rooftop-snipers': 'Engage in hilarious physics-based duels on city rooftops! Control wobbly characters armed with various weapons in this multiplayer shooting game. The unpredictable physics and simple controls create chaotic and entertaining battles perfect for quick competitive matches.',
  
  'roper': 'Swing through levels using precise rope mechanics! Time your swings perfectly to navigate through challenging obstacles and reach the finish line. This physics-based platformer requires skill and timing, offering a satisfying challenge for players who enjoy momentum-based gameplay.',

  // Car Games
  'car-rush': 'Race through traffic at high speeds while avoiding crashes! Weave between cars, collect coins, and upgrade your vehicle in this endless arcade racer. The simple tap controls and increasing speed create an adrenaline-pumping experience perfect for quick gaming sessions.',
  
  'crazy-cars': 'Perform insane stunts and races in physics-defying vehicles! Drive through loops, jumps, and impossible tracks while maintaining control of your crazy car. Each level offers unique challenges with creative track designs that push the limits of what cars can do.',
  
  'eggy-car': 'Transport a fragile egg through bumpy terrain without breaking it! This physics-based driving game challenges you to balance speed with caution as you navigate hills, valleys, and obstacles. The simple concept creates surprisingly addictive and tense gameplay moments.',
  
  'fire-truck': 'Rush to emergency scenes and put out fires in this action-packed simulation! Drive your fire truck through city streets, avoid traffic, and use your water cannon to extinguish flames. Time management and quick thinking are essential in this heroic rescue game.',
  
  'endless-truck': 'Drive massive trucks through endless highways and challenging terrain! Manage fuel, avoid obstacles, and deliver cargo safely across vast distances. The realistic truck physics and scenic routes create an immersive long-haul driving experience.',

  // Sports Games
  'basketball-legends-2020': 'Play as legendary basketball players in this arcade-style sports game! Choose from famous players, each with unique abilities and stats. Master different shot types, special moves, and tournament modes in this comprehensive basketball experience.',
  
  'basketball-line': 'Draw the perfect trajectory to score amazing basketball shots! Use physics and creativity to guide the ball into the hoop while avoiding obstacles. Each level presents new challenges that require both skill and creative problem-solving.',
  
  'basketball-stars': 'Compete in fast-paced basketball matches with arcade-style gameplay! Master timing, shooting, and defensive moves to outplay your opponents. The game features tournaments, multiplayer modes, and various courts for endless basketball action.',
  
  'basket-champs': 'Become the ultimate basketball champion in this skill-based sports game! Perfect your shooting technique, learn different shot types, and compete against increasingly difficult opponents. The progression system keeps you motivated to improve your skills.',

  // Jump & Run Games
  'doodle-jump': 'Jump as high as possible on endless platforms! Guide your character upward by tilting and avoid obstacles, monsters, and holes. Collect power-ups and achieve new height records in this addictive vertical platformer that started the endless jumping genre.',
  
  'fireboy-and-watergirl': 'Control two characters simultaneously in this cooperative puzzle platformer! Navigate through elemental temples where Fireboy and Watergirl must work together to solve puzzles, avoid hazards, and reach the exit. Perfect for single-player challenge or cooperative play.',
  
  'fireboy-and-watergirl-2': 'Continue the elemental adventure in the Light Temple! New light-based puzzles require both characters to manipulate mirrors, prisms, and light beams. The cooperative gameplay and clever level design make this sequel even more engaging than the original.',
  
  'fireboy-and-watergirl-3': 'Explore the Ice Temple where slippery surfaces add new challenges! Navigate through frozen environments where ice mechanics change how both characters move and interact with the world. The addition of ice physics creates fresh puzzle-solving opportunities.',
  
  'fireboy-and-watergirl-4': 'Venture into the Crystal Temple filled with teleportation portals! Use crystal portals to instantly transport between different areas while solving increasingly complex puzzles. The teleportation mechanic adds a new dimension to the cooperative gameplay.',
  
  'fireboy-and-watergirl-5': 'Master all elements in the Elements Temple! This culminating adventure combines mechanics from all previous games while introducing new challenges. Experience the ultimate test of cooperation and puzzle-solving skills.',
  
  'fireboy-and-watergirl-6': 'Discover the mysteries of the Fairy Temple with magical fairies! New fairy companions provide special abilities that help solve puzzles in creative ways. The addition of AI helpers creates unique gameplay dynamics.',

  // Shooting Games
  'apple-shooter': 'Test your archery skills in this precision shooting challenge! Aim carefully to hit apples placed on heads without harming the person below. Each successful shot increases the distance, making accuracy increasingly difficult and nerve-wracking.',
  
  'awesome-tanks-2': 'Command powerful tanks in strategic combat missions! Upgrade your tank with better weapons, armor, and special abilities as you battle through enemy territories. The combination of action and strategy creates engaging tactical gameplay.',
  
  'ballistic': 'Launch projectiles to destroy blocks in this physics-based puzzle shooter! Calculate angles and power to clear levels efficiently while dealing with moving obstacles and limited ammunition. The satisfying destruction and puzzle elements create addictive gameplay.',

  // Puzzle Games
  'ball-sort-puzzle': 'Sort colored balls into matching tubes in this relaxing puzzle game! Plan your moves carefully to organize all balls by color using limited space. The simple concept with increasingly complex arrangements creates a meditative yet challenging experience.',
  
  'ball-sort-halloween': 'Enjoy the classic ball sorting puzzle with spooky Halloween themes! Sort orange and black balls along with seasonal decorations while enjoying festive music and graphics. Perfect seasonal twist on the popular puzzle format.',
  
  'ball-sort-soccer': 'Combine your love of soccer with brain-teasing ball sorting puzzles! Sort soccer balls by team colors and patterns while enjoying football-themed graphics and sounds. A perfect blend of sports enthusiasm and puzzle solving.',
  
  'block-the-pig': 'Prevent the pig from escaping by strategically placing hexagonal blocks! Use logical thinking to trap the pig using the minimum number of moves. This brain teaser requires forward planning and spatial reasoning skills.',
  
  'checkers-legend': 'Master the classic strategy game of checkers with modern features! Play against AI opponents of varying difficulty levels or challenge friends in multiplayer mode. The timeless gameplay with smooth controls makes strategy accessible to all skill levels.',

  // Adventure Games
  'adam-and-eve-6': 'Help Adam navigate through prehistoric adventures to find Eve! Solve creative puzzles, interact with cavemen and dinosaurs, and overcome obstacles in this point-and-click adventure. The humorous storyline and clever puzzles create an entertaining experience.',
  
  'adam-and-eve-7': 'Continue Adams quest for love in this latest prehistoric adventure! Explore new environments, meet quirky characters, and solve increasingly challenging puzzles. The evolving storyline and creative problem-solving keep the series fresh and engaging.',
  
  'adam-and-eve-51': 'Experience another chapter in Adams ongoing romantic quest! Navigate through time-period challenges with creative thinking and problem-solving. Each level presents unique scenarios that require both logic and imagination to complete.',
  
  'adam-and-eve-52': 'Join Adam in his continued search for true love through various time periods! Solve environmental puzzles, interact with historical characters, and overcome obstacles using available tools. The blend of humor and challenging puzzles creates engaging gameplay.',
  
  'adventure-drivers': 'Race through diverse terrains in this action-packed driving adventure! Navigate through forests, deserts, and mountains while completing missions and collecting rewards. The variety of vehicles and environments keeps the adventure exciting and fresh.',

  // Age of War Games
  'age-of-war': 'Build your civilization through different historical eras! Start in the Stone Age and evolve through time by researching technologies, training armies, and defending your base. The strategic progression through history creates an epic warfare experience.',

  // Clicker Games
  'clicker-heroes': 'Click your way to heroic status in this addictive idle game! Defeat monsters, earn gold, hire heroes, and unlock powerful abilities. The progression system and idle mechanics make it perfect for both active play and passive progression.',
  
  'cookie-clicker-2': 'Bake your way to cookie empire domination! Click to produce cookies and purchase upgrades that automate and accelerate production. The satisfying progression and numerous upgrades create an incredibly addictive idle experience.',

  // Slime Games
  'blumgi-slime': 'Control a bouncy slime through colorful platform levels! Use unique slime physics to navigate obstacles, reach high platforms, and solve movement puzzles. The elastic mechanics and cheerful graphics create a fun and unique platforming experience.',
  
  'blumgi-rocket': 'Pilot rockets through challenging obstacle courses! Master thrust control and physics to navigate through tight spaces and reach the finish line. The precision required and satisfying rocket physics create an engaging flying challenge.',

  // Fighting Games
  'bomb-it-6': 'Engage in explosive multiplayer battles in classic Bomberman style! Place bombs strategically to eliminate opponents while avoiding your own explosions. The chaotic multiplayer action and power-ups create intense competitive gameplay.',
  
  'bomb-it-7': 'Continue the bombing mayhem with new arenas and features! Master bomb placement timing, collect power-ups, and outsmart opponents in various themed battlegrounds. The refined mechanics and new content enhance the explosive action.',

  // Idle/Merge Games
  'chicken-merge': 'Merge chickens to create more valuable poultry in this idle farming game! Combine identical chickens to evolve them into higher-tier birds that produce more eggs and income. The satisfying merge mechanics and cute graphics create relaxing gameplay.',
  
  'dinosaurs-merge-master': 'Collect and merge dinosaurs to build your prehistoric empire! Combine identical dinosaurs to create more powerful species while managing your Jurassic park. The evolution mechanics and dinosaur variety create an engaging collection experience.',

  // Music Games
  'friday-night-funkin': 'Battle through rhythm challenges in this viral music game! Hit arrow keys in sync with catchy beats while following storyline battles. The infectious soundtrack and challenging rhythm gameplay create an addictive musical experience perfect for music lovers.',
  
  // Restaurant Games
  'papa-louie': 'Manage Papa Louies restaurant empire in this time management simulation! Take orders, prepare food, and serve customers while upgrading your kitchen equipment. The strategic resource management and customer satisfaction elements create engaging restaurant gameplay.',
  
  'cooking-fever': 'Cook and serve dishes in fast-paced restaurant environments! Manage multiple orders simultaneously while upgrading kitchen equipment and decorations. The time pressure and strategic planning required create an exciting culinary challenge.',
  
  // Merge Games
  'merge-dragons': 'Combine magical creatures and items to heal corrupted lands! Merge identical objects to create more powerful versions while exploring fantasy worlds. The relaxing merge mechanics combined with progression elements create a satisfying puzzle experience.',
  
  '2048': 'Slide numbered tiles to combine them and reach the 2048 tile! Use strategic thinking to manage limited space while doubling numbers. This simple concept with mathematical progression creates incredibly addictive puzzle gameplay.',
  
  // Tower Defense Games
  'bloons-td': 'Defend against waves of colorful balloons using strategic tower placement! Upgrade and combine different tower types to create powerful defenses. The tower variety and upgrade paths create deep strategic gameplay with satisfying progression.',
  
  'kingdom-rush': 'Protect your kingdom from fantasy enemies using magical towers! Deploy heroes with special abilities while managing resources and upgrading defenses. The fantasy setting and hero progression create an epic tower defense experience.',
  
  // Word Games
  'wordle': 'Guess the hidden five-letter word in six attempts! Use logical deduction and vocabulary knowledge to solve daily word puzzles. The simple concept with daily challenges creates a perfect brain exercise for word enthusiasts.',
  
  'scrabble': 'Create words on the board using letter tiles for maximum points! Strategic tile placement and vocabulary knowledge determine victory. The classic word game mechanics provide timeless intellectual entertainment for all skill levels.',
  
  // Simulator Games
  'house-flipper': 'Buy, renovate, and sell houses for profit in this realistic simulation! Design interiors, repair damages, and make strategic investment decisions. The creative freedom and business management elements create a satisfying property development experience.',
  
  'farming-simulator': 'Manage a modern farm with realistic agricultural machinery! Plant crops, raise livestock, and expand your farming operation. The authentic farming mechanics and progression systems create an immersive rural life simulation.',
  
  // Survival Games
  'raft': 'Survive on a small raft in the middle of the ocean! Collect floating debris, purify water, and expand your floating home while avoiding shark attacks. The resource management and constant threat create intense survival gameplay.',
  
  'minecraft-classic': 'Build and explore in this classic block-based sandbox world! Mine resources, craft tools, and construct amazing structures limited only by imagination. The creative freedom and exploration elements provide endless entertainment possibilities.',
  
  // Throwing Games  
  'angry-birds': 'Launch birds at pig fortresses using physics-based slingshot mechanics! Aim carefully to destroy structures and defeat all pigs with limited birds. The satisfying physics destruction and puzzle solving create addictive casual gameplay.',
  
  'basketball-throw': 'Perfect your basketball shooting skills in this arcade sports game! Adjust angle and power to score baskets from various distances and angles. The realistic ball physics and scoring challenges create engaging athletic gameplay.',
  
  // Truck Games
  'truck-simulator': 'Drive massive trucks across realistic highway systems! Manage fuel, follow traffic rules, and deliver cargo safely across long distances. The authentic truck physics and route planning create an immersive long-haul driving experience.',
  
  'monster-truck': 'Crush obstacles with powerful monster trucks in extreme terrain! Navigate through mud, rocks, and ramps while maintaining vehicle control. The dramatic physics and spectacular crashes create thrilling off-road racing action.',
  
  // Bike Games
  'bike-race': 'Perform spectacular stunts and races on motorcycles! Navigate through challenging tracks while maintaining balance and speed. The physics-based controls and track variety create exciting two-wheeled racing adventures.',
  
  'happy-wheels': 'Navigate dangerous obstacle courses with various characters and vehicles! The ragdoll physics and creative level design create hilariously chaotic gameplay perfect for players who enjoy physics-based challenges.',
  
  // Bus Games  
  'bus-simulator': 'Drive city buses through realistic urban environments! Follow schedules, pick up passengers, and navigate traffic while providing public transportation services. The authentic city driving and time management create a realistic transit experience.',
  
  'school-bus': 'Safely transport students to school while navigating busy streets! Follow traffic rules, manage time schedules, and ensure passenger safety. The responsibility and precision required create engaging educational transportation gameplay.',
  
  // Adventure Games Extended
  'minecraft-dungeons': 'Explore dangerous dungeons filled with monsters and treasures! Battle through procedurally generated levels while collecting loot and upgrading equipment. The action RPG elements and cooperative gameplay create exciting dungeon-crawling adventures.',
  
  'terraria': 'Dig, build, and fight in this 2D sandbox adventure world! Mine resources, craft equipment, and battle bosses while exploring vast underground caverns. The crafting depth and exploration elements provide hundreds of hours of adventure gameplay.',
  
  // Additional Popular Games
  'slope': 'Control a ball rolling down an endless neon slope! Avoid obstacles and holes while the speed continuously increases. The simple controls and intense action create an addictive arcade experience perfect for quick gaming sessions.',
  
  'run-3': 'Navigate through space tunnels in this endless running adventure! Jump and run through gravity-defying levels while avoiding gaps and obstacles. The unique space setting and physics mechanics create a distinctive running experience.',
  
  'paper-io': 'Claim territory by drawing lines and closing shapes! Expand your area while avoiding other players and protecting your borders. The simple concept with competitive multiplayer elements creates addictive territorial gameplay.',
  
  'hole-io': 'Control a black hole that grows by consuming objects! Start small and gradually devour larger items while competing against other holes. The satisfying growth mechanics and competitive elements create engaging multiplayer action.',
  
  'slither-io': 'Grow your snake by eating glowing orbs in this multiplayer arena! Avoid other snakes while trying to make them crash into you. The classic snake game concept with modern multiplayer twist creates addictive competitive gameplay.',
  
  'agar-io': 'Control a cell that grows by absorbing smaller cells! Split and merge strategically while avoiding larger players. The simple biological concept with complex strategy elements creates engaging multiplayer survival gameplay.',
  
  // Fighting Games Extended  
  'street-fighter': 'Master martial arts combat in this classic fighting game! Learn special moves, combos, and character abilities while battling opponents. The deep combat system and character variety create competitive fighting experiences.',
  
  'mortal-kombat': 'Engage in brutal fighting tournaments with iconic characters! Execute fatalities, special moves, and devastating combos. The mature combat system and dramatic finishing moves create intense fighting game action.',
  
  // Sports Games Extended
  'fifa-soccer': 'Experience realistic soccer matches with professional teams! Control players, execute strategies, and score goals in authentic stadium environments. The realistic physics and team management create immersive football simulation.',
  
  'nba-basketball': 'Play professional basketball with realistic team rosters! Master dribbling, shooting, and defensive strategies while competing in tournaments. The authentic sport mechanics and player abilities create engaging basketball simulation.',
  
  // Additional Card Games
  'solitaire': 'Play the classic card game with traditional rules! Organize cards by suit and number while using strategic thinking. The timeless gameplay and multiple difficulty levels provide relaxing yet challenging card entertainment.',
  
  'poker': 'Master the art of poker with various game modes! Learn hand rankings, betting strategies, and psychological tactics. The skill-based gameplay and strategic depth create engaging card game experiences.',
  
  'blackjack': 'Beat the dealer by getting as close to 21 as possible! Make strategic decisions about hitting, standing, and doubling down. The mathematical strategy and quick decision-making create exciting casino-style gameplay.',
  
  // Other Popular Games
  '1010-color-match': 'Arrange colorful blocks in this addictive puzzle game! Drag and drop different shaped pieces to fill rows and columns completely. The Tetris-inspired mechanics with strategic planning create satisfying puzzle-solving experiences perfect for quick mental breaks.',
  
  '3-pandas-in-japan': 'Help three adorable pandas navigate through Japanese adventures! Solve environmental puzzles, interact with local culture, and overcome obstacles using teamwork. The charming characters and creative problem-solving create delightful family-friendly gameplay.',
  
  '3d-bowling': 'Experience realistic bowling physics in this 3D sports simulation! Master ball control, spin techniques, and pin targeting to achieve strikes and spares. The authentic bowling mechanics and tournament modes create engaging sporting competition.',
  
  '8-ball-pool': 'Play professional pool matches with realistic physics and controls! Master cue positioning, spin effects, and strategic shot selection in various game modes. The precision required and competitive multiplayer options create authentic billiards experiences.',
  
  'adventure-drivers': 'Race through diverse terrains while completing challenging missions! Navigate mountains, forests, and deserts in various vehicles while collecting rewards and unlocking new content. The adventure elements and racing action create exciting exploration gameplay.',
  
  'ball-sort-halloween': 'Sort spooky Halloween-themed balls in this seasonal puzzle! Organize orange, black, and themed balls into matching containers using logical thinking. The festive graphics and relaxing gameplay create perfect autumn entertainment.',
  
  'ball-sort-soccer': 'Combine soccer passion with brain-teasing ball sorting puzzles! Sort soccer balls by team colors and patterns while enjoying football-themed environments. The sports theme adds excitement to classic puzzle mechanics.',
  
  'basket-and-ball': 'Master basketball shooting mechanics in this physics-based sports game! Calculate trajectories and power to score baskets from challenging angles. The realistic ball physics and progressive difficulty create satisfying athletic challenges.',
  
  'biker-street': 'Race motorcycles through busy city streets and highways! Navigate traffic, perform stunts, and customize your bike while earning money. The urban racing environment and bike customization create thrilling street racing experiences.',
  
  'bob-the-robber-2': 'Sneak through buildings as a master thief in this stealth puzzle adventure! Avoid guards, disable security systems, and steal valuable items using clever strategies. The stealth mechanics and puzzle elements create engaging criminal gameplay.',
  
  'fireboy-and-watergirl-2': 'Continue the elemental cooperation in the Light Temple! Use light beams, mirrors, and crystals to solve puzzles requiring both characters. The innovative light-based mechanics add new dimensions to cooperative puzzle-solving.',
  
  'fireboy-and-watergirl-3': 'Explore the challenging Ice Temple where slippery surfaces change everything! Navigate frozen environments where ice physics affect movement and puzzle solutions. The winter theme and ice mechanics create fresh cooperative challenges.',
  
  'fireboy-and-watergirl-4': 'Master teleportation in the mysterious Crystal Temple! Use crystal portals to transport between areas while solving increasingly complex puzzles. The teleportation mechanics add strategic depth to cooperative gameplay.',
  
  'fireboy-and-watergirl-5': 'Experience the ultimate elements challenge in the Elements Temple! Combine all previous mechanics while introducing new obstacles and puzzles. This culminating adventure tests all cooperative skills developed throughout the series.',
  
  'fireboy-and-watergirl-6': 'Discover magical assistance in the enchanting Fairy Temple! Work with helpful fairies that provide unique abilities to solve creative puzzles. The AI companion mechanics create new cooperative dynamics.',
  
  'fish-eat-fish': 'Survive in underwater ecosystems where bigger fish eat smaller ones! Grow your fish by consuming smaller creatures while avoiding larger predators. The natural food chain mechanics create intense survival gameplay with constant progression.',
  
  'fishing-and-lines': 'Cast your line and catch various fish species in relaxing fishing simulation! Master different fishing techniques, upgrade equipment, and explore multiple fishing locations. The peaceful gameplay and progression systems create meditative outdoor experiences.',
  
  'fishing-frenzy': 'Experience fast-paced fishing action with time pressure and challenges! Catch as many fish as possible while managing limited time and competing objectives. The arcade-style mechanics and urgency create exciting aquatic competitions.',
  
  'five-nights-at-freddys': 'Survive terrifying nights as a security guard in this horror game! Monitor animatronic characters through security cameras while managing limited power supply. The psychological horror and resource management create intense survival experiences.',
  
  'five-nights-at-freddys-2': 'Face new animatronic threats in this horror sequel! Use updated security systems and strategies to survive against more aggressive enemies. The enhanced horror elements and new mechanics increase the terror and challenge.',
  
  'five-nights-at-freddys-3': 'Confront the horror legacy in the final installment! Navigate through decrepit facilities while avoiding the ultimate animatronic threat. The concluding storyline and refined horror mechanics create climactic survival horror.',
  
  'five-nights-at-freddys-4': 'Experience childhood nightmares in this psychological horror prequel! Defend against nightmare animatronics using different survival strategies. The domestic setting and audio-focused gameplay create uniquely terrifying experiences.',
  
  'five-nights-at-freddys-5': 'Enter the Sister Location facility in this horror adventure! Navigate through maintenance areas while avoiding new animatronic dangers. The facility exploration and story elements expand the horror universe.',
  
  'freecell-solitaire': 'Master this strategic solitaire variant with open foundation piles! Use free cells strategically to organize cards by suit and sequence. The skill-based gameplay and unlimited undos create satisfying card puzzle experiences.',
  
  'friday-night-funkin': 'Battle through musical rap battles in this rhythm phenomenon! Hit arrow keys in perfect sync with catchy beats while following storyline conflicts. The infectious music and challenging rhythm gameplay create addictive musical entertainment.',
  
  'fruit-ninja': 'Slice flying fruits with precise finger swipes in this action game! Avoid bombs while creating satisfying fruit combinations and achieving high scores. The simple yet addictive slicing mechanics create perfect casual gaming experiences.',
  
  'g-switch': 'Defy gravity in this fast-paced running platformer! Switch gravity direction to navigate through challenging obstacle courses at high speed. The gravity mechanics and precise timing create unique endless running experiences.',
  
  'g-switch-2': 'Continue gravity-defying adventures with new challenges and features! Master advanced gravity switching techniques while navigating more complex environments. The refined mechanics and increased difficulty enhance the gravity-based gameplay.',
  
  'g-switch-3': 'Experience the ultimate gravity switching challenge with multiplayer modes! Compete against friends while mastering gravity control in various game modes. The competitive elements and social features expand the gravity-based fun.',
  
  'g-switch-4': 'Master the latest gravity switching mechanics with enhanced features! Navigate through evolved challenges that test gravity control skills to the limit. The advanced mechanics and refined gameplay create the definitive gravity-switching experience.',
  
  'geometry-dash': 'Navigate through rhythm-based obstacle courses with precise timing! Jump and fly through geometric challenges synchronized to energetic soundtracks. The music synchronization and precise controls create incredibly addictive platforming experiences.',
  
  'gobdun': 'Explore dangerous dungeons filled with monsters and treasures! Battle through procedurally generated levels while collecting loot and upgrading equipment. The dungeon crawler mechanics and RPG progression create engaging adventure experiences.',
  
  'golf-battle': 'Compete in mini golf tournaments with physics-based gameplay! Master ball control and course strategy while challenging opponents in multiplayer matches. The competitive golf mechanics and course variety create engaging sporting entertainment.',
  
  'highway-rider-extreme': 'Race motorcycles at extreme speeds through heavy traffic! Weave between cars, perform stunts, and customize bikes while earning money. The high-speed action and bike customization create thrilling highway racing adventures.',
  
  'hop-pop-it': 'Experience the satisfying sensation of popping bubbles in this relaxing game! Pop colorful bubbles in various patterns while enjoying stress-relief gameplay. The simple mechanics and satisfying feedback create perfect relaxation entertainment.',
  
  'idle-breakout': 'Break blocks automatically in this idle version of the classic game! Upgrade balls and abilities while blocks break themselves continuously. The idle progression and classic arcade mechanics create addictive incremental gameplay.',
  
  'idle-mining-empire': 'Build a mining empire that runs itself in this idle simulation! Automate mining operations, upgrade equipment, and expand territories while earning passive income. The business management and idle progression create engaging tycoon experiences.',
  
  'idle-restaurants': 'Manage restaurant chains that operate automatically! Upgrade kitchens, hire staff, and expand locations while earning passive restaurant income. The food service theme and idle mechanics create satisfying business simulation.',
  
  'iron-snout': 'Fight off wolves as a brave pig using martial arts moves! Master combat combinations and defensive techniques while battling increasing enemy waves. The action combat and character progression create entertaining fighting experiences.',
  
  'jelly-truck': 'Drive wobbly jelly trucks through challenging obstacle courses! Navigate through levels where the truck\'s jelly physics create unique driving challenges. The unusual vehicle mechanics and creative level design provide distinctive racing fun.',
  
  'klondike-solitaire': 'Play the classic Klondike solitaire with traditional rules! Organize cards in foundation piles by suit while using strategic tableau moves. The timeless card game mechanics provide perfect mental exercise and relaxation.',
  
  'monkey-mart': 'Manage a busy mart run by adorable monkeys! Stock shelves, serve customers, and expand the store while upgrading facilities and staff. The cute characters and business management create charming simulation experiences.',
  
  'moto-x3m': 'Perform spectacular motorcycle stunts on challenging obstacle courses! Navigate through loops, jumps, and hazards while maintaining speed and balance. The physics-based controls and creative track design create thrilling stunt racing.',
  
  'moto-x3m-2': 'Continue extreme motorcycle stunts with new tracks and challenges! Master advanced techniques while navigating through more complex obstacle courses. The enhanced track variety and refined mechanics improve upon the original formula.',
  
  'moto-x3m-4-winter': 'Experience winter-themed motorcycle stunt challenges! Navigate through snowy tracks with icy conditions that affect bike handling. The seasonal theme and weather mechanics add fresh challenges to stunt racing.',
  
  'moto-x3m-5-pool-party': 'Perform aquatic stunts in this summer-themed motorcycle adventure! Race through water parks and poolside tracks with splashing effects. The water theme and beach atmosphere create refreshing stunt racing experiences.',
  
  'moto-x3m-6-spooky-land': 'Navigate through haunted motorcycle tracks in this horror-themed racing game! Perform stunts while avoiding spooky obstacles and Halloween decorations. The horror theme adds atmospheric excitement to stunt racing.',
  
  'mr-bullet': 'Solve shooting puzzles that require strategic thinking and precision! Calculate angles and ricochets to eliminate targets efficiently using limited ammunition. The puzzle elements and physics mechanics create engaging tactical challenges.',
  
  'mr-bullet-3d': 'Experience three-dimensional shooting puzzles with enhanced graphics! Master 3D trajectory calculations while solving increasingly complex target challenges. The dimensional depth and visual improvements enhance the tactical shooting experience.',
  
  'neon-biker': 'Race through futuristic neon-lit environments on high-tech motorcycles! Navigate glowing tracks while enjoying cyberpunk aesthetics and electronic music. The visual style and futuristic setting create immersive racing experiences.',
  
  'neon-racer': 'Experience high-speed racing in vibrant neon environments! Drive through glowing tracks with electronic music while avoiding obstacles at extreme speeds. The cyberpunk aesthetics and fast-paced action create exciting futuristic racing.',
  
  'park-master': 'Master the art of parallel parking in challenging scenarios! Navigate tight spaces while avoiding obstacles and other vehicles. The realistic parking physics and progressive difficulty create satisfying driving skill challenges.',
  
  'parking-fury': 'Navigate through complex parking challenges with precision driving! Maneuver through tight spaces, avoid collisions, and park perfectly within time limits. The parking scenarios and realistic physics create engaging driving puzzles.',
  
  'parking-fury-2': 'Continue mastering parking skills with new vehicles and challenges! Experience enhanced parking scenarios with improved graphics and mechanics. The expanded content and refined gameplay improve upon the original parking formula.',
  
  'pou': 'Care for your virtual pet Pou in this interactive simulation! Feed, clean, and play with your pet while customizing its appearance and environment. The pet care mechanics and customization options create engaging virtual companion experiences.',
  
  'racing-monster-trucks': 'Drive massive monster trucks through extreme terrain! Crush obstacles, perform jumps, and navigate challenging courses with powerful vehicles. The oversized vehicles and destructive gameplay create spectacular racing action.',
  
  'raft-wars': 'Engage in strategic water battles using makeshift rafts and weapons! Calculate angles and power to defeat enemies while defending your territory. The strategy elements and physics-based combat create engaging tactical warfare.',
  
  'raft-wars-2': 'Continue aquatic warfare with enhanced weapons and challenges! Master advanced combat techniques while facing tougher enemies and situations. The improved mechanics and expanded content enhance the strategic water battle experience.',
  
  'rocket-league': 'Play soccer with rocket-powered cars in this unique sports game! Master car control, aerial maneuvers, and team strategies while scoring goals. The innovative concept and competitive gameplay create addictive vehicular sports action.',
  
  'snake-vs-block': 'Control a growing snake that breaks through numbered blocks! Strategically navigate through barriers while managing snake length and avoiding obstacles. The mathematical progression and strategic elements create engaging puzzle action.',
  
  'space-bar-clicker': 'Test your clicking speed and endurance in this simple yet addictive game! Click the spacebar as rapidly as possible while competing for high scores. The minimal mechanics and competitive elements create surprisingly engaging clicking challenges.',
  
  'spider-solitaire': 'Master this challenging solitaire variant with multiple suits! Organize cards in descending sequences while clearing all cards from the tableau. The complex strategy and multiple difficulty levels provide excellent card game challenges.',
  
  'stick-merge': 'Merge stick figures to create more powerful characters! Combine identical units to evolve them into stronger versions while building your army. The merge mechanics and character progression create satisfying idle strategy gameplay.',
  
  'stick-merge-2': 'Continue stick figure evolution with enhanced merging mechanics! Master advanced combination strategies while building more diverse character armies. The improved systems and expanded content enhance the merge strategy experience.',
  
  'stickman-fighter-epic-battles': 'Control stickman warriors in epic combat scenarios! Master fighting moves, weapon combat, and tactical strategies while battling multiple enemies. The action combat and character progression create engaging fighting adventures.',
  
  'subway-surfers': 'Run through subway tunnels while avoiding trains and obstacles! Collect coins, use power-ups, and customize characters while achieving distance records. The endless running mechanics and urban setting create addictive pursuit gameplay.',
  
  'temple-run': 'Escape from ancient temples while being chased by monsters! Navigate through ruins, collect gems, and use abilities while avoiding deadly obstacles. The atmospheric setting and pursuit mechanics create thrilling adventure experiences.',
  
  'tiny-fishing': 'Experience relaxing fishing in this idle simulation game! Cast lines automatically while upgrading equipment and exploring different fishing spots. The peaceful mechanics and progression systems create meditative fishing entertainment.',
  
  'tower-crash-3d': 'Destroy towering structures using strategic ball throws! Calculate angles and power to demolish buildings efficiently while earning points. The destruction physics and strategic elements create satisfying demolition gameplay.',
  
  'toy-defense': 'Defend against toy soldier invasions using strategic tower placement! Build and upgrade defensive structures while managing resources efficiently. The toy theme and tower defense mechanics create charming strategic warfare.',
  
  'tri-peaks-solitaire': 'Clear three pyramid peaks in this engaging solitaire variant! Remove cards in sequence while using strategic thinking and planning. The unique layout and progression mechanics create distinctive card game challenges.',
  
  'truck-trials': 'Navigate heavy trucks through challenging terrain and obstacles! Master truck physics while delivering cargo safely through difficult courses. The realistic vehicle handling and cargo management create authentic trucking experiences.',
  
  'tunnel-rush': 'Race through colorful tunnels at incredible speeds while avoiding obstacles! Navigate through geometric patterns and tight spaces while the speed continuously increases. The hypnotic visuals and intense action create thrilling racing experiences.',
  
  'volleyball-challenge': 'Compete in volleyball matches with realistic physics and controls! Master serving, spiking, and defensive techniques while competing in tournaments. The authentic volleyball mechanics create engaging sporting competition.',
  
  'word-slide': 'Form words by sliding letter tiles in this brain-teasing puzzle! Connect adjacent letters to create valid words while clearing the board efficiently. The word formation mechanics and strategic tile movement create educational entertainment.',
  
  'wordle-unlimited': 'Guess five-letter words in this unlimited version of the popular puzzle! Use logical deduction and vocabulary knowledge to solve word challenges without daily limits. The endless gameplay and word mechanics provide continuous brain exercise.',
  
  // Extended Game Collection
  'bottle-flip': 'Master the art of bottle flipping in this physics-based skill game! Time your flips perfectly to land bottles upright on various surfaces and obstacles. The simple concept with precise physics creates surprisingly challenging and addictive gameplay.',
  
  'bouncy-woods': 'Navigate through forest levels using bouncing mechanics! Control a bouncy character through tree-filled environments while avoiding obstacles and collecting items. The spring-based physics and natural setting create a unique platforming experience.',
  
  'bubble-pop-adventures': 'Pop colorful bubbles in this match-three puzzle adventure! Aim and shoot bubbles to create groups of three or more identical colors. The progression through levels with increasing challenges creates addictive puzzle-solving gameplay.',
  
  'bus-parking-3d': 'Master the art of parking large buses in tight spaces! Navigate through realistic 3D environments while avoiding obstacles and other vehicles. The challenging parking scenarios and realistic physics create an authentic driving simulation experience.',
  
  'cubefield': 'Navigate through an endless field of cubes at high speed! Steer left and right to avoid hitting the geometric obstacles while the speed continuously increases. The minimalist design and intense action create a hypnotic and challenging experience.',
  
  'dead-again': 'Survive in this intense action game filled with zombies and challenges! Fight through hordes of undead enemies using various weapons and strategies. The survival horror elements and combat mechanics create a thrilling and dangerous experience.',
  
  'e-scooter': 'Ride electric scooters through urban environments! Navigate city streets, avoid traffic, and complete delivery missions while managing battery life and speed. The modern urban setting and eco-friendly theme create a contemporary gaming experience.'
};

// Function to show game description tooltip
function showGameTooltip(gameKey, event) {
  const description = gameDescriptions[gameKey];
  if (!description) return;
  
  // Remove existing tooltip
  const existingTooltip = document.querySelector('.game-tooltip');
  if (existingTooltip) {
    existingTooltip.remove();
  }
  
  // Create tooltip element
  const tooltip = document.createElement('div');
  tooltip.className = 'game-tooltip';
  tooltip.innerHTML = description;
  
  // Style the tooltip
  tooltip.style.cssText = `
    position: fixed;
    background: rgba(0, 0, 0, 0.9);
    color: white;
    padding: 12px 16px;
    border-radius: 8px;
    font-size: 14px;
    line-height: 1.4;
    max-width: 320px;
    z-index: 10000;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    border: 1px solid rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    pointer-events: none;
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.3s ease;
  `;
  
  document.body.appendChild(tooltip);
  
  // Position tooltip
  const rect = event.target.closest('.col').getBoundingClientRect();
  const tooltipRect = tooltip.getBoundingClientRect();
  
  let left = rect.left + (rect.width / 2) - (tooltipRect.width / 2);
  let top = rect.bottom + 10;
  
  // Keep tooltip in viewport
  if (left + tooltipRect.width > window.innerWidth - 10) {
    left = window.innerWidth - tooltipRect.width - 10;
  }
  if (left < 10) {
    left = 10;
  }
  if (top + tooltipRect.height > window.innerHeight - 10) {
    top = rect.top - tooltipRect.height - 10;
  }
  
  tooltip.style.left = left + 'px';
  tooltip.style.top = top + 'px';
  
  // Animate in
  setTimeout(() => {
    tooltip.style.opacity = '1';
    tooltip.style.transform = 'translateY(0)';
  }, 10);
}

// Function to hide game description tooltip
function hideGameTooltip() {
  const tooltip = document.querySelector('.game-tooltip');
  if (tooltip) {
    tooltip.style.opacity = '0';
    tooltip.style.transform = 'translateY(10px)';
    setTimeout(() => {
      if (tooltip.parentNode) {
        tooltip.parentNode.removeChild(tooltip);
      }
    }, 300);
  }
}

// Function to extract game key from URL
function getGameKeyFromUrl(url) {
  const match = url.match(/\/([^\/]+)-unblocked\.html$/);
  if (match) {
    return match[1];
  }
  return null;
}

// Initialize tooltips for game elements
function initGameTooltips() {
  document.querySelectorAll('#gamelist-1 .col a').forEach(link => {
    const gameKey = getGameKeyFromUrl(link.getAttribute('href'));
    if (gameKey && gameDescriptions[gameKey]) {
      link.addEventListener('mouseenter', (e) => showGameTooltip(gameKey, e));
      link.addEventListener('mouseleave', hideGameTooltip);
      link.addEventListener('click', hideGameTooltip);
    }
  });
}

// Initialize when DOM is loaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initGameTooltips);
} else {
  initGameTooltips();
}
