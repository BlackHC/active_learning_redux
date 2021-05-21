store = {}
store['timestamp']=1621471665
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=4']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=4
store['worker_id']=4
store['num_workers']=80
store['config']={'seed': 1238, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.0615382194519043})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.4197230339050293})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.558882713317871})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9552721977233887})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.9500293731689453})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6985, 'crossentropy': 2.21062734375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.148491621017456})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1224756240844727})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0989280939102173})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1340277194976807})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 51137], ['id', 34678], ['id', 20751], ['id', 32453], ['id', 18971]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.1422374101359214, 2.0059793662524403, 2.6364275878738708, 3.049379475110129, 3.28838054285361]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.8749518394470215})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.255199909210205})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.424952507019043})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.758086681365967})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.6437690258026123})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.7927985191345215})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.814260244369507})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.794001579284668})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6757, 'crossentropy': 2.5005361328125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.1841297149658203})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1997333765029907})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1736947298049927})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.167302131652832})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 46941], ['id', 40057], ['id', 3782], ['id', 7389], ['id', 43073]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9665031276219125, 1.7031913020066565, 2.2524688723313444, 2.611882642025746, 2.8200462592612325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.808292269706726})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.9617135524749756})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.3433432579040527})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.077366352081299})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7133, 'crossentropy': 1.523272265625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.179147481918335})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1000920534133911})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1007676124572754})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 23482], ['id', 36805], ['id', 16558], ['id', 29239], ['id', 14655]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7635861387191696, 1.354570430497465, 1.8448008895493961, 2.22822495503792, 2.5068297387725167]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.3706210851669312})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.5009945631027222})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.8108019828796387})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.967665672302246})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.788991928100586})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.8916162252426147})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.9166241884231567})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.9785079956054688})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 2.1102492809295654})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 2.0208606719970703})
store['active_learning_steps'][3]['training']['best_epoch']=7
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7944, 'crossentropy': 1.64767734375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9062505960464478})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.841406524181366})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.8338808417320251})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.7958967685699463})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.8108377456665039})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 32323], ['id', 41999], ['id', 28712], ['id', 55853], ['id', 41019]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9013473432055259, 1.6778165707627108, 2.307122808700747, 2.719033320502307, 2.9339875822310155]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.422520637512207})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.4740471839904785})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.7061975002288818})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.783904790878296})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.828647255897522})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.8749407529830933})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.9649455547332764})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7638, 'crossentropy': 1.660105859375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.0387494564056396})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.8990880250930786})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.8526962995529175})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.874455988407135})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 0.8895071744918823})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 50054], ['id', 12595], ['id', 25246], ['id', 22564], ['id', 52908]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9086308987327518, 1.6971523877340688, 2.2570267427634887, 2.6477308150147145, 2.864972563095696]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.2022775411605835})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.503462791442871})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.6238718032836914})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.6811559200286865})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.6510536670684814})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.7126834392547607})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.8001811504364014})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.9632015228271484})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.9149904251098633})
store['active_learning_steps'][5]['training']['best_epoch']=6
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8031, 'crossentropy': 1.57004462890625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.8902624845504761})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.8198390603065491})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.7913126945495605})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8063253164291382})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.8129010796546936})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.7734075784683228})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.7931243181228638})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.7982034683227539})
store['active_learning_steps'][5]['eval_training']['best_epoch']=6
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 7621], ['id', 14536], ['id', 4335], ['id', 5593], ['id', 49549]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.9492075423564397, 1.7079908947294604, 2.3240472409827726, 2.7465696859424433, 2.97149771459861]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1202948093414307})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.2690114974975586})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.3152873516082764})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.5796241760253906})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.5477161407470703})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.4619667530059814})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.5489845275878906})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.5468266010284424})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.5947710275650024})
store['active_learning_steps'][6]['training']['best_epoch']=6
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8334, 'crossentropy': 1.29183271484375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.834782600402832})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7199141979217529})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7143099904060364})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.7340251803398132})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7092214822769165})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 15304], ['id', 18386], ['id', 52123], ['id', 11853], ['id', 42161]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7929312129029091, 1.4926930894313513, 2.0422129131455096, 2.3907465385389433, 2.6058309756903277]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0964248180389404})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2419381141662598})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.3168245553970337})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.3129647970199585})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.825, 'crossentropy': 0.961271484375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9147697687149048})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.8071513772010803})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.7903800010681152})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 40905], ['id', 54316], ['id', 27641], ['id', 17339], ['id', 30444]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7446408495844874, 1.3213759372756506, 1.817884839019528, 2.1841796191215597, 2.457137668212731]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.076027274131775})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1232719421386719})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2057640552520752})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.28792405128479})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.2002946138381958})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.3961074352264404})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8346, 'crossentropy': 0.98193330078125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8273407816886902})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.74826979637146})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.7315075993537903})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.7496776580810547})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.7394673824310303})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 35786], ['id', 45313], ['id', 16866], ['id', 2548], ['id', 48912]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7476389377872976, 1.344033448375126, 1.822705447461355, 2.1834982694916256, 2.4188764450008717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9762558937072754})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9415759444236755})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9849825501441956})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0966333150863647})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1796531677246094})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1545848846435547})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8676, 'crossentropy': 0.85376162109375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7304539680480957})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6421018838882446})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6042453050613403})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.5886170864105225})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.5760069489479065})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 54043], ['id', 29472], ['id', 58401], ['id', 3648], ['id', 377]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7563168357790087, 1.3678462383671026, 1.865129327171589, 2.225621494612075, 2.47827519580615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9091707468032837})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8434650897979736})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9432684183120728})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0366432666778564})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9942766427993774})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0775169134140015})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8731, 'crossentropy': 0.7929537109375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7760311365127563})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.621496319770813})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.5841128826141357})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.5735330581665039})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5576283931732178})
store['active_learning_steps'][10]['eval_training']['best_epoch']=5
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 57392], ['id', 23795], ['id', 8719], ['id', 30097], ['id', 16620]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7592345126300819, 1.4447803969532371, 2.0123846667394485, 2.386501651034342, 2.6414980228647504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8055243492126465})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8094372153282166})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8819694519042969})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8802586793899536})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9679214954376221})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.077225685119629})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8881, 'crossentropy': 0.71301416015625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6967644691467285})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.5999732613563538})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.5971940755844116})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5502808094024658})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.5812571048736572})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 43711], ['id', 43000], ['id', 45346], ['id', 42607], ['id', 36818]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.8278035867548907, 1.4297489851266398, 1.940755945401201, 2.3006519675509463, 2.550645539518534]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8073727488517761})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7691780924797058})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8244372606277466})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8994253873825073})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8840240240097046})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.0121421813964844})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9158389568328857})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.0388847589492798})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8934, 'crossentropy': 0.74541962890625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7214610576629639})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5901098251342773})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.541405200958252})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5311876535415649})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5352827310562134})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5442707538604736})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 43224], ['id', 41283], ['id', 33150], ['id', 43455], ['id', 49883]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8442150934533608, 1.5385683361899192, 2.080235741386656, 2.4263169674022516, 2.6254528799154517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9366652965545654})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7564258575439453})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7896912097930908})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7757042050361633})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8523659706115723})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8668482303619385})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8986, 'crossentropy': 0.628350537109375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6936280727386475})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5521494150161743})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5434106588363647})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5155147314071655})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5107860565185547})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 42821], ['id', 35110], ['id', 44928], ['id', 24285], ['id', 5400]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7487582395033936, 1.3361728057165934, 1.838611385164164, 2.21464374035307, 2.4391546310084697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8837906718254089})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7368402481079102})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6876720190048218})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7449121475219727})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9158097505569458})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8575118184089661})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8086627721786499})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8873262405395508})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9574776887893677})
store['active_learning_steps'][14]['training']['best_epoch']=6
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9133, 'crossentropy': 0.6445630859375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6771199107170105})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5423467755317688})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.49423229694366455})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.44361692667007446})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4591047763824463})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.45290547609329224})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.43496173620224})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.45019304752349854})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 24360], ['id', 22633], ['id', 53379], ['id', 36055], ['id', 11342]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7808029752776786, 1.482484323282141, 2.054881405988744, 2.4233025354131508, 2.621600911805632]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7439827919006348})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6345215439796448})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7497355937957764})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7342434525489807})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7574988603591919})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8642932772636414})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8437631130218506})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8981506824493408})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9112, 'crossentropy': 0.604581640625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6633906364440918})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5259389281272888})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.48275911808013916})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4582104980945587})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.4479462504386902})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.45006024837493896})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.45781368017196655})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 26240], ['id', 54387], ['id', 45047], ['id', 28253], ['id', 16919]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7409893638957754, 1.3810393178519718, 1.8950855542294764, 2.2645146124765816, 2.462505723040045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8120099306106567})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6031548976898193})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5744892358779907})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6727252006530762})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6194901466369629})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7544063329696655})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7345786094665527})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8353573083877563})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7849175930023193})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7261559367179871})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9179, 'crossentropy': 0.6051552734375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6851135492324829})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5410113334655762})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.44500112533569336})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.43993404507637024})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.41975492238998413})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.3873673975467682})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4103151559829712})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4110793173313141})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.39852261543273926})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 12702], ['id', 57523], ['id', 32794], ['id', 9396], ['id', 47452]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7926180306037831, 1.4942929240316452, 2.0796334702675, 2.4259953135244707, 2.600492195595418]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8238999843597412})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6601347923278809})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5929936170578003})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6465790271759033})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6984074711799622})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6554716229438782})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6923446655273438})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7460330724716187})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7389258146286011})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9149, 'crossentropy': 0.60401552734375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6973303556442261})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.49235332012176514})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.46067410707473755})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.42985236644744873})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.41291260719299316})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4353731572628021})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.3955635130405426})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.40785813331604004})
store['active_learning_steps'][17]['eval_training']['best_epoch']=8
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 22579], ['id', 34800], ['id', 37347], ['id', 28632], ['id', 25446]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7698007948861278, 1.4509767594230225, 2.006800007630633, 2.397975821842703, 2.622131109918934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.83774733543396})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5857382416725159})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6195768117904663})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6024410724639893})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7075956463813782})
store['active_learning_steps'][18]['training']['best_epoch']=2
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9091, 'crossentropy': 0.56075576171875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7088977098464966})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.566832959651947})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5204033851623535})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4845270812511444})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 19396], ['id', 11708], ['id', 11877], ['id', 31736], ['id', 18003]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6374029866174444, 1.2121786273233237, 1.6882262214431805, 2.0821045690452076, 2.333718152314165]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8878151178359985})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6160175800323486})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6470142602920532})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7186890244483948})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.647488534450531})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7344980239868164})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.712485134601593})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6953210830688477})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6639286875724792})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7459132671356201})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6890543699264526})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9226, 'crossentropy': 0.59289990234375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6540466547012329})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5225076675415039})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4675988256931305})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.42261314392089844})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4253770411014557})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.42643439769744873})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.43585699796676636})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 16036], ['id', 27653], ['id', 36401], ['id', 5851], ['id', 25823]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7912621369207427, 1.5060182439220555, 2.0852618503743825, 2.512134394025918, 2.7787290176045794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7745006084442139})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5274425148963928})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5761189460754395})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6028074026107788})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5421667098999023})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5701320171356201})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.500815869140625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.570920467376709})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.48821210861206055})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.44311320781707764})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4102819561958313})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.42872530221939087})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 47732], ['id', 14749], ['id', 14872], ['id', 43897], ['id', 53693]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6358937332734838, 1.2165639688963257, 1.6988969670222094, 2.069129520641196, 2.311857285689107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8069853782653809})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5752293467521667})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5283629894256592})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5662742853164673})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5567286014556885})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5248571038246155})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5461889505386353})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6464710235595703})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6219244599342346})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.934, 'crossentropy': 0.495404443359375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6563242673873901})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4448348879814148})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.38151127099990845})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.35519158840179443})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3615555167198181})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3234555721282959})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.34333011507987976})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.33881354331970215})
store['active_learning_steps'][21]['eval_training']['best_epoch']=7
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 27514], ['id', 4481], ['id', 47936], ['id', 27739], ['id', 39080]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8117662157981358, 1.4466529418098535, 1.9157920208318036, 2.2342776527850825, 2.4345316897804246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9372640252113342})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5706694722175598})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5259939432144165})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49514248967170715})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5265898704528809})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5602213740348816})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5475718379020691})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5590099692344666})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.933, 'crossentropy': 0.46933212890625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6511254906654358})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4542294144630432})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3930795192718506})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.40090417861938477})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.36550068855285645})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3619183599948883})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.36096179485321045})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 26358], ['id', 41289], ['id', 18041], ['id', 44051], ['id', 28267]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6614628987885616, 1.2655189451718654, 1.7794836122195656, 2.1560442986338204, 2.4130564034510105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8259665369987488})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5111657381057739})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5262402296066284})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5004186630249023})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5361588001251221})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9272, 'crossentropy': 0.486291064453125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7297232747077942})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5475583672523499})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.497275710105896})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.48009026050567627})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 20641], ['id', 6898], ['id', 10744], ['id', 50639], ['id', 14689]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6386603988771438, 1.206076647611369, 1.691174038236234, 1.998136165669413, 2.2171815079054404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8768930435180664})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.47324076294898987})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47736507654190063})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.481841504573822})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4765235185623169})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4975346326828003})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9377, 'crossentropy': 0.43270859375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.660027265548706})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.45444387197494507})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.408215194940567})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3912065029144287})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.37977397441864014})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 16756], ['id', 39208], ['id', 20161], ['id', 30584], ['id', 52959]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6740078649240469, 1.245832437951269, 1.6815403258693413, 2.0243536498141186, 2.2511029215942475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8332366943359375})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5394743084907532})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.46542084217071533})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.46688902378082275})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.541575014591217})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5135695934295654})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5884818434715271})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5038125514984131})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5300809144973755})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.943, 'crossentropy': 0.430937451171875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6855493783950806})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.493833988904953})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4074997007846832})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4024496078491211})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.35899949073791504})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3453139364719391})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.33596333861351013})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34051448106765747})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 38082], ['id', 45062], ['id', 19937], ['id', 32190], ['id', 54730]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7772557137985818, 1.4243778392169357, 1.9585539841377662, 2.348466916046301, 2.623948279141552]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.844464898109436})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4898398518562317})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.434187114238739})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45624232292175293})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44773223996162415})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5104053020477295})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5294966697692871})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48948878049850464})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9418, 'crossentropy': 0.4027119140625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6530243158340454})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.44880443811416626})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.40925586223602295})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3742510676383972})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3683660328388214})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3496791124343872})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3528628349304199})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 11192], ['id', 11020], ['id', 32738], ['id', 41540], ['id', 16301]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6679199813603725, 1.271898140156054, 1.7659217237070468, 2.1301933353321596, 2.3694980675301007]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9785712957382202})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5568180680274963})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5017062425613403})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48912182450294495})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43157556653022766})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4904313087463379})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5095571279525757})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5144474506378174})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9459, 'crossentropy': 0.374501123046875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6775093674659729})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.45177605748176575})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3831339478492737})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.36296072602272034})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3689691722393036})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3699963092803955})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3347722589969635})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 57728], ['id', 11044], ['id', 18419], ['id', 20072], ['id', 2761]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.588473556525063, 1.1422464162855936, 1.6209788288986369, 1.978122405493286, 2.2299590091737365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9024271368980408})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5259836912155151})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5699654817581177})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.46204909682273865})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.453411340713501})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4469589591026306})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5006321668624878})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.46803992986679077})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.521373987197876})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9464, 'crossentropy': 0.38396416015625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7322407960891724})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.46588999032974243})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.41467440128326416})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3576706647872925})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3303884267807007})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34019044041633606})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3195872902870178})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.2975727915763855})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 26918], ['id', 26577], ['id', 44382], ['id', 4611], ['id', 10844]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7049915441866039, 1.2961829761568247, 1.729632638232312, 2.0433990716879658, 2.257432969045852]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8620694875717163})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5517137050628662})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.47278010845184326})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4261844754219055})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4713522791862488})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4575777053833008})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5352872014045715})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9415, 'crossentropy': 0.3949850830078125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7377661466598511})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4637414216995239})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.42533236742019653})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.383861780166626})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.35223495960235596})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3514195382595062})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 59287], ['id', 22083], ['id', 13428], ['id', 19412], ['id', 7380]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6480617554700645, 1.204143937346402, 1.675259339546976, 2.0130272180280953, 2.2340815963758214]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9625170826911926})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5790702104568481})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4243554472923279})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4443569779396057})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3989993929862976})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.45801445841789246})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5312793254852295})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5123048424720764})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9494, 'crossentropy': 0.345659619140625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7452564239501953})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47910118103027344})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.421893835067749})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.37690800428390503})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3369629383087158})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3398531675338745})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.32727837562561035})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 18049], ['id', 33401], ['id', 31915], ['id', 34429], ['id', 11767]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6513832823644656, 1.2265901894813567, 1.731349683502037, 2.1140080346161554, 2.3258646824486595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9090797305107117})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5203077793121338})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41761916875839233})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42208510637283325})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4522515833377838})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3942111134529114})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.44749969244003296})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4438138008117676})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4267125129699707})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.48820191621780396})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4334809184074402})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4658099412918091})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4761320948600769})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45797690749168396})
store['active_learning_steps'][31]['training']['best_epoch']=11
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9507, 'crossentropy': 0.3887889404296875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7254819869995117})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.45223110914230347})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3493375778198242})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.34164124727249146})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3222185969352722})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.31439098715782166})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.30442142486572266})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.2979314923286438})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3025912046432495})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.2871079444885254})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2635830342769623})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.2944507598876953})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2945272922515869})
store['active_learning_steps'][31]['eval_training']['best_epoch']=11
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 32668], ['id', 32499], ['id', 40040], ['id', 23346], ['id', 21066]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7520437591729154, 1.3999104064461063, 1.928030767318691, 2.3276554664751368, 2.577028966752745]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0103812217712402})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5207692384719849})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.40401792526245117})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42712897062301636})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.48796015977859497})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9402, 'crossentropy': 0.4537501953125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7446063756942749})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.588750422000885})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.555594801902771})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5156614184379578})
store['active_learning_steps'][32]['eval_training']['best_epoch']=3
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 43126], ['id', 20170], ['id', 39999], ['id', 15500], ['id', 20709]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5389229712092287, 1.0081925973390429, 1.4001550586143852, 1.7131947428428163, 1.9722206595379284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1258220672607422})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5442674160003662})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4187740683555603})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3926001191139221})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3641894459724426})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40933042764663696})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4029473066329956})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4108344614505768})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3777092397212982})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9547, 'crossentropy': 0.366558251953125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.667783260345459})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4742986261844635})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.386200487613678})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3681657910346985})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3514699637889862})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3531302213668823})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.33347269892692566})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3294993042945862})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 35406], ['id', 36783], ['id', 57718], ['id', 40654], ['id', 39539]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6050999853315044, 1.129683223894605, 1.5947774321998311, 1.9695023900334077, 2.240057680143474]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0044124126434326})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46124058961868286})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4077775180339813})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37411123514175415})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41450560092926025})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43734705448150635})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.944, 'crossentropy': 0.4026750244140625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8280164003372192})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5139588713645935})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47262582182884216})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4548946022987366})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4379236102104187})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 51047], ['id', 49607], ['id', 4058], ['id', 35326], ['id', 5738]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6160314571400134, 1.1806140715305102, 1.642983342547848, 2.0016568800961263, 2.263598844147465]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0458341836929321})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6060218811035156})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4313347339630127})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4059317409992218})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.41564124822616577})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4121530055999756})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44684213399887085})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9471, 'crossentropy': 0.377108544921875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6920453906059265})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4581012725830078})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4251486659049988})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37984341382980347})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37659940123558044})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3760560154914856})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 20110], ['id', 854], ['id', 36434], ['id', 38920], ['id', 4212]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6083560716727268, 1.1892852623719836, 1.6814482351035824, 2.0294051494837344, 2.2735385855592183]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0207270383834839})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4877772927284241})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42378127574920654})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4186002314090729})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4021369516849518})
store['active_learning_steps'][36]['training']['best_epoch']=2
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.946, 'crossentropy': 0.447785546875}
