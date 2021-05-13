store = {}
store['timestamp']=1620296688
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=14']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=14
store['worker_id']=14
store['num_workers']=40
store['config']={'seed': 17, 'acquisition_size': 20, 'max_training_set': 450, 'num_pool_samples': 100, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.BALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.342047929763794})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.767544746398926})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.0798144340515137})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.883221387863159})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6694, 'crossentropy': 2.0522388671875}
store['active_learning_steps'][0]['acquisition']={'indices': [56775, 46036, 56777, 11762, 542, 39527, 46707, 56004, 32784, 19042, 33126, 25341, 33835, 34678, 28226, 43081, 51761, 13549, 4727, 13551], 'labels': [0, 2, 0, 9, 0, 0, 2, 8, 8, 9, 9, 8, 0, 8, 8, 0, 9, 8, 8, 5], 'scores': [1.216804027557373, 1.2161849737167358, 1.2114309072494507, 1.208348274230957, 1.2021284699440002, 1.1852413415908813, 1.1826976537704468, 1.181555986404419, 1.1813968420028687, 1.179886281490326, 1.1798135042190552, 1.1777194738388062, 1.1731704473495483, 1.1721609830856323, 1.170175850391388, 1.168381929397583, 1.1675985455513, 1.1673918962478638, 1.1663585901260376, 1.1661336421966553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.1465954780578613})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.2866742610931396})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.588836908340454})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.5952558517456055})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6411, 'crossentropy': 1.9261947265625}
store['active_learning_steps'][1]['acquisition']={'indices': [39130, 13309, 36492, 12447, 39963, 21210, 27641, 12950, 59924, 32427, 13303, 21880, 49179, 41557, 12117, 12223, 22477, 53019, 51400, 15641], 'labels': [6, 6, 8, 2, 4, 5, 2, 2, 6, 0, 6, 2, 2, 0, 3, 2, 3, 2, 6, 6], 'scores': [0.9737133979797363, 0.9657258987426758, 0.9656487703323364, 0.960016667842865, 0.9599659442901611, 0.9430117607116699, 0.9365999698638916, 0.9338591694831848, 0.9280418753623962, 0.9261434674263, 0.9200978875160217, 0.9147141575813293, 0.9146131873130798, 0.9145338535308838, 0.9125304222106934, 0.912423849105835, 0.912063717842102, 0.909515380859375, 0.9083025455474854, 0.9081826210021973]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.4762591123580933})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.859792947769165})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.341130256652832})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.240828037261963})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.735, 'crossentropy': 1.32736640625}
store['active_learning_steps'][2]['acquisition']={'indices': [56698, 32126, 9046, 42368, 28375, 32301, 47028, 57985, 13471, 37758, 16176, 29390, 13030, 25998, 8580, 27120, 40701, 6258, 43904, 28720], 'labels': [4, 4, 4, 7, 5, 4, 4, 4, 4, 0, 2, 9, 0, 7, 4, 2, 7, 4, 4, 5], 'scores': [0.973275363445282, 0.9592306017875671, 0.9393446445465088, 0.923418402671814, 0.9192183613777161, 0.9182419180870056, 0.9115756154060364, 0.908695638179779, 0.9022178649902344, 0.9004549980163574, 0.8996564149856567, 0.8961407542228699, 0.8887170553207397, 0.8879870176315308, 0.8878647089004517, 0.8860632181167603, 0.8822699785232544, 0.8797006011009216, 0.8788710832595825, 0.8760841488838196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.1678386926651})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.3703300952911377})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.3251357078552246})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.6662352085113525})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7873, 'crossentropy': 1.0486341796875}
store['active_learning_steps'][3]['acquisition']={'indices': [53989, 28455, 8411, 11154, 1356, 49354, 21009, 22661, 25359, 26020, 26534, 57728, 49117, 42680, 50308, 43978, 57242, 47643, 21385, 21433], 'labels': [2, 5, 2, 5, 5, 0, 2, 2, 5, 5, 3, 9, 3, 5, 3, 3, 5, 3, 5, 5], 'scores': [0.7782579064369202, 0.7660150527954102, 0.7588765621185303, 0.7360698580741882, 0.7322578430175781, 0.7318670749664307, 0.7181313037872314, 0.7156004309654236, 0.7150954008102417, 0.7110788822174072, 0.7109842300415039, 0.7098802328109741, 0.7068206071853638, 0.7064759135246277, 0.7017223238945007, 0.700813889503479, 0.7002054452896118, 0.6993572115898132, 0.6992020606994629, 0.6979176998138428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.201827049255371})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.2386375665664673})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2553839683532715})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.4787176847457886})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7746, 'crossentropy': 1.0774296875}
store['active_learning_steps'][4]['acquisition']={'indices': [10910, 2862, 9180, 37044, 29132, 2777, 7168, 33812, 12595, 15484, 19040, 58415, 27992, 20050, 25102, 23140, 5129, 39409, 47039, 49091], 'labels': [6, 6, 3, 6, 8, 6, 8, 6, 4, 6, 6, 6, 6, 9, 6, 7, 2, 5, 5, 3], 'scores': [0.7897842526435852, 0.7880667448043823, 0.7837408185005188, 0.7798066735267639, 0.7759089469909668, 0.7720261812210083, 0.7613790035247803, 0.7605040669441223, 0.7568875551223755, 0.7545862197875977, 0.752907395362854, 0.7510901093482971, 0.7510203123092651, 0.7492069005966187, 0.7466984391212463, 0.7437479496002197, 0.7424268126487732, 0.7412314414978027, 0.741162896156311, 0.7406724691390991]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.045969009399414})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.940984845161438})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0017400979995728})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0640569925308228})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.1640024185180664})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8544, 'crossentropy': 0.83179423828125}
store['active_learning_steps'][5]['acquisition']={'indices': [12181, 4646, 34328, 6474, 49517, 40775, 39281, 17005, 14394, 13259, 34765, 20855, 33035, 36417, 35537, 41537, 44365, 24589, 8867, 30441], 'labels': [5, 2, 8, 6, 6, 6, 1, 1, 3, 1, 6, 6, 6, 6, 6, 3, 6, 8, 8, 1], 'scores': [0.9645111560821533, 0.9506186842918396, 0.913632333278656, 0.9118664264678955, 0.8999465703964233, 0.8976282477378845, 0.8862627744674683, 0.8861461877822876, 0.88297039270401, 0.8788081407546997, 0.8758177757263184, 0.8671998977661133, 0.8618535995483398, 0.8604752421379089, 0.8580683469772339, 0.8578200936317444, 0.8576446175575256, 0.8565813302993774, 0.8548225164413452, 0.8499947786331177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.9499673843383789})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.757909893989563})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8859139084815979})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9054226279258728})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.949134111404419})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8915, 'crossentropy': 0.670671923828125}
store['active_learning_steps'][6]['acquisition']={'indices': [19638, 10044, 39700, 32348, 8488, 7833, 50782, 31545, 43176, 16406, 47828, 1024, 33222, 49348, 13460, 49548, 34406, 15778, 50223, 43048], 'labels': [5, 6, 5, 5, 6, 5, 5, 5, 2, 5, 5, 5, 5, 5, 5, 8, 4, 5, 5, 5], 'scores': [0.9882251024246216, 0.9525730013847351, 0.9359968304634094, 0.9311443567276001, 0.9175127446651459, 0.9158082604408264, 0.909703254699707, 0.9004730582237244, 0.8965178728103638, 0.8914920687675476, 0.8913794159889221, 0.8885893821716309, 0.8851301670074463, 0.8846122026443481, 0.8808569312095642, 0.871544599533081, 0.8604061007499695, 0.8580024242401123, 0.8578755259513855, 0.8568611145019531]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.0718472003936768})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8681638240814209})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8954406976699829})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8020771145820618})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9302377104759216})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8442990183830261})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9484049677848816})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.894, 'crossentropy': 0.71274931640625}
store['active_learning_steps'][7]['acquisition']={'indices': [52358, 16860, 2856, 47068, 28373, 18365, 30464, 39487, 18998, 47505, 1674, 54878, 33162, 26693, 55282, 36704, 20653, 59390, 14411, 47425], 'labels': [2, 8, 4, 4, 4, 4, 4, 2, 2, 8, 9, 4, 8, 4, 4, 2, 4, 2, 4, 8], 'scores': [1.0413872599601746, 1.0387828946113586, 1.0361929535865784, 1.030963659286499, 1.007789671421051, 0.9888665676116943, 0.9866064786911011, 0.9813470840454102, 0.980181097984314, 0.9781578183174133, 0.9748930931091309, 0.9642128348350525, 0.9636087417602539, 0.9623342156410217, 0.9576044082641602, 0.9538659453392029, 0.9498415589332581, 0.9493739008903503, 0.9451481699943542, 0.9419431090354919]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.0203355550765991})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6564915180206299})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6922297477722168})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6884877681732178})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7604522109031677})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8834, 'crossentropy': 0.66600869140625}
store['active_learning_steps'][8]['acquisition']={'indices': [42428, 44898, 1518, 12752, 134, 9036, 40576, 11693, 14901, 55235, 41489, 44736, 14367, 12840, 13138, 35351, 49537, 58840, 37489, 59297], 'labels': [5, 2, 9, 2, 1, 2, 4, 3, 2, -1, 2, 5, 3, 9, 2, 7, 2, -1, 2, 1], 'scores': [0.866874098777771, 0.8264655470848083, 0.8190042972564697, 0.8182975053787231, 0.8182226419448853, 0.8136570453643799, 0.8110053539276123, 0.8087568283081055, 0.8009185791015625, 0.7997642755508423, 0.7985868453979492, 0.7950998544692993, 0.7905398607254028, 0.7903281450271606, 0.7897356748580933, 0.7896947264671326, 0.7831227779388428, 0.7817555665969849, 0.7815195918083191, 0.7813906669616699]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.1364641189575195})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7193695306777954})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7720552682876587})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6836521625518799})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6729706525802612})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.758051872253418})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7421118021011353})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7592008113861084})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9105, 'crossentropy': 0.6438890625}
store['active_learning_steps'][9]['acquisition']={'indices': [22525, 42711, 28783, 50461, 41307, 36613, 4421, 30451, 28641, 32918, 57325, 8559, 25551, 56472, 28723, 57547, 5959, 37974, 40457, 42269], 'labels': [4, 4, 7, 7, 4, 7, 7, 8, 7, 2, 7, 7, -1, 7, 7, 7, 7, 2, 0, 7], 'scores': [1.0778186321258545, 1.0449382066726685, 1.0339041948318481, 1.0099583864212036, 0.9977342486381531, 0.996799647808075, 0.9939173460006714, 0.9920868873596191, 0.9904870390892029, 0.9873478412628174, 0.9858036041259766, 0.9740506410598755, 0.9698699116706848, 0.9694128632545471, 0.9682720899581909, 0.9640273451805115, 0.9636567831039429, 0.9628425240516663, 0.9565094709396362, 0.9561840295791626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.0550270080566406})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.6935054063796997})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6952831745147705})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6405736207962036})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8033992052078247})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8512169122695923})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7717783451080322})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9031, 'crossentropy': 0.59328359375}
store['active_learning_steps'][10]['acquisition']={'indices': [3615, 36587, 28930, 2137, 33461, 17283, 49767, 59726, 34520, 4360, 52140, 13945, 47260, 9447, 37115, 49364, 6019, 2633, 43663, 14715], 'labels': [6, 9, 7, 9, 9, 9, 9, 5, 6, 6, 4, 9, 6, 9, 9, 7, 9, 9, 9, 4], 'scores': [1.0327028036117554, 0.9892668128013611, 0.983430802822113, 0.9395700693130493, 0.9389508962631226, 0.9387953877449036, 0.938381016254425, 0.9244871139526367, 0.9222292900085449, 0.9198132157325745, 0.9101141095161438, 0.9098167419433594, 0.9091801643371582, 0.9033538103103638, 0.9027432203292847, 0.8994098901748657, 0.8946419954299927, 0.8926066160202026, 0.8896358013153076, 0.883340060710907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.08100426197052})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5828213095664978})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5106419920921326})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5387798547744751})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.49775704741477966})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5116412043571472})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5437772274017334})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5507597327232361})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9301, 'crossentropy': 0.48716455078125}
store['active_learning_steps'][11]['acquisition']={'indices': [42703, 49525, 4955, 16756, 49064, 19586, 35971, 35246, 58413, 52889, 37469, 6309, 966, 46379, 17409, 28199, 54954, 4611, 49624, 6251], 'labels': [0, 8, 2, 7, 8, 9, 0, 8, 9, -1, 2, 3, 3, 3, 3, 3, 8, -1, 6, 3], 'scores': [0.9504402875900269, 0.9274454116821289, 0.9185158610343933, 0.9167979955673218, 0.9163384437561035, 0.9139675498008728, 0.9101736545562744, 0.9060061573982239, 0.9058800339698792, 0.8973190784454346, 0.8951007127761841, 0.8887228965759277, 0.886868953704834, 0.8833577632904053, 0.8825705051422119, 0.8814501464366913, 0.88062584400177, 0.8800826668739319, 0.8769009411334991, 0.8748793601989746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0899467468261719})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.602798342704773})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4967151880264282})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5244036912918091})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4720286726951599})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4923301339149475})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4914981722831726})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5297633409500122})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9314, 'crossentropy': 0.485369140625}
store['active_learning_steps'][12]['acquisition']={'indices': [3768, 14697, 18398, 52462, 13969, 7886, 16692, 49153, 13942, 14722, 13998, 52889, 27429, 23350, 45911, 27344, 59681, 8978, 14201, 56152], 'labels': [5, 8, 4, 9, 3, 9, 5, 6, 4, 0, 9, -1, 0, 8, 3, 9, 0, 2, 7, 9], 'scores': [1.0238919258117676, 0.9374356865882874, 0.933029055595398, 0.9264020919799805, 0.921625554561615, 0.9169641733169556, 0.9164304733276367, 0.9136795997619629, 0.9127563238143921, 0.9125565886497498, 0.9113207459449768, 0.9106634855270386, 0.9098067879676819, 0.9019427299499512, 0.8931818008422852, 0.8919552564620972, 0.8907709717750549, 0.8887268304824829, 0.8818308115005493, 0.878914475440979]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0606046915054321})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5886372327804565})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5267956256866455})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4973253011703491})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.45216602087020874})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46271294355392456})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4814128279685974})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4670799970626831})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9408, 'crossentropy': 0.4331083984375}
store['active_learning_steps'][13]['acquisition']={'indices': [38577, 13253, 53187, 42337, 37413, 45437, 43126, 35109, 15913, 52294, 50993, 16855, 7917, 44350, 17367, 4193, 45385, 12937, 5429, 1597], 'labels': [5, 5, 1, 5, 5, 1, 3, 1, 9, 0, 1, 1, 5, 3, 1, 1, 1, 5, 1, 1], 'scores': [1.0564942359924316, 1.009839415550232, 0.9826027154922485, 0.9793282151222229, 0.9625089168548584, 0.9618500471115112, 0.9604033827781677, 0.9442274570465088, 0.9417077302932739, 0.9357814788818359, 0.9285983443260193, 0.9254598617553711, 0.924951434135437, 0.9237188100814819, 0.9236083030700684, 0.9226685762405396, 0.9223254919052124, 0.9218470454216003, 0.9214980006217957, 0.9209649562835693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0312005281448364})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5761745572090149})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4856681823730469})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4539262056350708})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4367164075374603})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4863092303276062})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5066112875938416})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5236435532569885})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.944, 'crossentropy': 0.42773349609375}
store['active_learning_steps'][14]['acquisition']={'indices': [51863, 42787, 45069, 24479, 3644, 57311, 32513, 16011, 42004, 29180, 8459, 42292, 28362, 38178, 8879, 56006, 5155, 18951, 38165, 1846], 'labels': [9, 4, 4, 8, 1, 5, 4, 5, 7, 9, 5, 7, 7, 7, 3, 3, 4, 7, 5, 7], 'scores': [0.9844425916671753, 0.9338619709014893, 0.9167110323905945, 0.9031848311424255, 0.9019778966903687, 0.899966835975647, 0.8989717960357666, 0.8934884071350098, 0.8856827020645142, 0.8846383690834045, 0.8826802372932434, 0.8820669651031494, 0.876862108707428, 0.8696120977401733, 0.8659552335739136, 0.8655878901481628, 0.864456295967102, 0.8608298897743225, 0.8588228821754456, 0.8559163212776184]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9551022052764893})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5667992830276489})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4415401816368103})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41652607917785645})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4287480115890503})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46840888261795044})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3902507424354553})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41259390115737915})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.46985775232315063})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4349241852760315})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.954, 'crossentropy': 0.363867529296875}
store['active_learning_steps'][15]['acquisition']={'indices': [32519, 49202, 59468, 1075, 20169, 23956, 27503, 34115, 27791, 43772, 23028, 52685, 9458, 28293, 41266, 13156, 41334, 1127, 18418, 6846], 'labels': [5, 5, 7, 7, 4, 4, 2, 5, -1, 5, 2, -1, -1, 2, 1, 2, 9, 7, 5, 2], 'scores': [1.0669912099838257, 0.9901886582374573, 0.9742624759674072, 0.9695838689804077, 0.9689781069755554, 0.9652854800224304, 0.963624119758606, 0.9626918435096741, 0.9615238904953003, 0.9582356810569763, 0.9520134031772614, 0.9470325112342834, 0.9458206295967102, 0.9456080794334412, 0.9434766173362732, 0.9399285316467285, 0.9393689632415771, 0.9393351674079895, 0.9387961626052856, 0.9381915926933289]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.025441288948059})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5786182880401611})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5333024263381958})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4571987986564636})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4692556858062744})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48755431175231934})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4604223072528839})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9441, 'crossentropy': 0.41132978515625}
store['active_learning_steps'][16]['acquisition']={'indices': [14385, 43823, 22531, 52089, 36818, 10992, 58560, 24424, 31252, 14619, 26850, 37048, 44172, 15106, 57882, 12768, 43606, 43042, 33505, 24325], 'labels': [8, 8, 4, 7, 7, -1, 0, 1, 5, 3, 2, 9, 8, 7, 0, 9, -1, 8, 2, -1], 'scores': [0.8886828422546387, 0.8713027834892273, 0.8704565763473511, 0.8687371015548706, 0.847822368144989, 0.8411083221435547, 0.8396013975143433, 0.8359458446502686, 0.8342940807342529, 0.8282890915870667, 0.8266582489013672, 0.8220690488815308, 0.8214938640594482, 0.8172135353088379, 0.8104615211486816, 0.8080554008483887, 0.8073902726173401, 0.8063018918037415, 0.8051860332489014, 0.8048491477966309]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0852757692337036})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6154327392578125})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5116609334945679})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4646221995353699})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4541264772415161})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45174267888069153})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42847371101379395})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42697209119796753})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4535706043243408})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5015857219696045})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5060364007949829})
store['active_learning_steps'][17]['training']['best_epoch']=8
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9503, 'crossentropy': 0.396795556640625}
store['active_learning_steps'][17]['acquisition']={'indices': [26389, 32776, 48540, 36072, 59314, 54981, 20859, 40066, 25551, 32668, 26785, 26754, 6466, 37583, 44570, 228, 1512, 59081, 8940, 5443], 'labels': [0, 4, 8, 2, 9, 2, 8, 4, -1, 9, 6, 6, 2, -1, 7, 3, 0, -1, 6, -1], 'scores': [0.9559099674224854, 0.9505398273468018, 0.9445440173149109, 0.9374880194664001, 0.9372788667678833, 0.9295125007629395, 0.9293050169944763, 0.9253172874450684, 0.9225795269012451, 0.9180018901824951, 0.9128736257553101, 0.9108747839927673, 0.9064831733703613, 0.9042063355445862, 0.897798478603363, 0.8948512673377991, 0.8948498964309692, 0.8940801024436951, 0.8934862613677979, 0.8902370929718018]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1135635375976562})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5724619030952454})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.47951382398605347})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44467413425445557})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42052483558654785})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3577460050582886})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38511741161346436})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3777610659599304})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.42247962951660156})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9537, 'crossentropy': 0.3712495849609375}
store['active_learning_steps'][18]['acquisition']={'indices': [47568, 50840, 36810, 42784, 9472, 19546, 11292, 9390, 46132, 48360, 12702, 18003, 4005, 4904, 1812, 49890, 53211, 4153, 32880, 11616], 'labels': [7, 2, 6, 7, 2, 9, 1, 9, 7, 3, 3, 2, 2, 7, 4, 5, -1, 2, 0, 7], 'scores': [0.9558901190757751, 0.9102441072463989, 0.900180995464325, 0.895954430103302, 0.8911376595497131, 0.8850420117378235, 0.8831825256347656, 0.8561190962791443, 0.8490754961967468, 0.8430712819099426, 0.8403109908103943, 0.8401205539703369, 0.8395191431045532, 0.8333720564842224, 0.8318493962287903, 0.8304646611213684, 0.8304572701454163, 0.8274078965187073, 0.8259986042976379, 0.8234541416168213]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.1120086908340454})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6016425490379333})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40753546357154846})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3914281725883484})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3516969680786133})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41248762607574463})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3628164827823639})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36429059505462646})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9593, 'crossentropy': 0.3146942626953125}
store['active_learning_steps'][19]['acquisition']={'indices': [59747, 12066, 27791, 48681, 16036, 59731, 19868, 55739, 13031, 47328, 3251, 13677, 45422, 13021, 28357, 22139, 21674, 27172, 30478, 39457], 'labels': [5, 8, -1, 2, 8, 5, 5, 5, 2, 8, 8, 8, 0, 5, 0, 2, 2, 3, 8, 0], 'scores': [0.9145928025245667, 0.8822077512741089, 0.8703477382659912, 0.8633015155792236, 0.8301894664764404, 0.8171036243438721, 0.8139484524726868, 0.812424898147583, 0.8073433637619019, 0.8044252395629883, 0.801389217376709, 0.7988452315330505, 0.7980949878692627, 0.7973229885101318, 0.7961139678955078, 0.7944267392158508, 0.7934810519218445, 0.7923264503479004, 0.7884511947631836, 0.7882726192474365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1981401443481445})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.598466157913208})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42516446113586426})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.369157612323761})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3483656048774719})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35966500639915466})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31551146507263184})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35148558020591736})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3319995105266571})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.360107958316803})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.3044525146484375}
store['active_learning_steps'][20]['acquisition']={'indices': [18501, 10746, 17739, 36828, 37672, 58024, 29672, 21390, 38142, 55620, 59701, 7160, 8447, 7606, 45954, 49524, 47936, 9309, 602, 52719], 'labels': [4, 9, 5, 8, 8, 8, 9, 3, 8, 8, 5, 1, 3, 8, 8, 6, 8, 8, 8, 8], 'scores': [1.0345926880836487, 1.008535921573639, 1.0034170150756836, 0.992918074131012, 0.992917001247406, 0.9620535969734192, 0.9593600630760193, 0.9539458751678467, 0.9530084133148193, 0.9505183696746826, 0.9396049976348877, 0.938073456287384, 0.9373512268066406, 0.927483320236206, 0.9246477484703064, 0.9217063188552856, 0.9134615063667297, 0.9112560749053955, 0.9084402322769165, 0.906708836555481]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.1773903369903564})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6440092325210571})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4137434959411621})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3643122613430023})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3568994402885437})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4075515866279602})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3420794606208801})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36441662907600403})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3466501533985138})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34781455993652344})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.961, 'crossentropy': 0.3497936279296875}
store['active_learning_steps'][21]['acquisition']={'indices': [31184, 32047, 51464, 40378, 19702, 58379, 1160, 23086, 53990, 27791, 50317, 27085, 6582, 39561, 19824, 40768, 12663, 60, 36008, 35336], 'labels': [9, 9, 0, -1, 5, -1, 4, 8, -1, -1, 3, 8, 8, 2, 9, -1, 8, 4, 8, -1], 'scores': [1.0001867413520813, 0.9716923236846924, 0.9497640132904053, 0.9318951964378357, 0.9301526546478271, 0.9271899461746216, 0.922575831413269, 0.9215463399887085, 0.9200012683868408, 0.919999897480011, 0.9144979119300842, 0.9135423302650452, 0.9123929738998413, 0.9082299470901489, 0.907015860080719, 0.904676079750061, 0.9018503725528717, 0.901451587677002, 0.9001643061637878, 0.899484395980835]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.1386888027191162})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6761355996131897})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4423776865005493})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4687315821647644})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3965408205986023})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3764845132827759})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3478013277053833})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31750398874282837})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3551567792892456})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4047088921070099})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37766459584236145})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9655, 'crossentropy': 0.3360705810546875}
store['active_learning_steps'][22]['acquisition']={'indices': [41789, 39076, 52889, 1015, 49889, 42028, 7558, 32747, 32108, 28030, 20172, 34707, 2803, 11572, 54832, 37578, 18563, 18598, 50407, 7949], 'labels': [0, 1, -1, 0, 0, 1, -1, 8, 4, 0, 4, 8, 3, 5, 0, -1, 0, 9, 0, -1], 'scores': [1.0275093913078308, 0.9714754819869995, 0.9700198173522949, 0.9553127884864807, 0.9498212933540344, 0.948610246181488, 0.9376546144485474, 0.9350763559341431, 0.9346253871917725, 0.9309579730033875, 0.9299370050430298, 0.9294468760490417, 0.9278687238693237, 0.9239198565483093, 0.922028124332428, 0.9219995141029358, 0.9203980565071106, 0.9169780015945435, 0.9166032075881958, 0.9154358506202698]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.2689176797866821})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6521379947662354})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4673280715942383})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.39708131551742554})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3036283850669861})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3063890337944031})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33753448724746704})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3377177119255066})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.3326940673828125}
